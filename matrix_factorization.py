import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Model
from keras.layers import Input
from keras.layers.core import Reshape
from keras.layers.merge import Multiply
from keras.layers.merge import Dot
from keras.layers.embeddings import Embedding
from keras import optimizers
import keras
import tensorflow as tf
from keras import regularizers


def plot_model_history(model_history):
    fig, axs = plt.subplots(1,2,figsize=(15,5))
    # summarize history for accuracy
    axs[0].plot(range(1,len(model_history.history['acc'])+1),model_history.history['acc'])
    axs[0].plot(range(1,len(model_history.history['val_acc'])+1),model_history.history['val_acc'])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    axs[0].set_xticks(np.arange(1,len(model_history.history['acc'])+1),len(model_history.history['acc'])/10)
    axs[0].legend(['train', 'val'], loc='best')
    # summarize history for loss
    axs[1].plot(range(1,len(model_history.history['loss'])+1),model_history.history['loss'])
    axs[1].plot(range(1,len(model_history.history['val_loss'])+1),model_history.history['val_loss'])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].set_xticks(np.arange(1,len(model_history.history['loss'])+1),len(model_history.history['loss'])/10)
    axs[1].legend(['train', 'val'], loc='best')
    plt.show()


sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
keras.backend.set_session(sess)

data = pd.read_csv('data/ratings.csv',names=["User","Anime","Rating"])
user_count,item_count = len(data.User.unique()),len(data.Anime.unique())

user_id_input = Input(shape=[1], name='user')
item_id_input = Input(shape=[1], name='item')

embedding_size = 30
user_embedding = Embedding(output_dim=embedding_size, input_dim=user_count,
                           input_length=1, name='user_embedding',embeddings_regularizer=regularizers.l2(0.0001))(user_id_input)
item_embedding = Embedding(output_dim=embedding_size, input_dim=item_count,
                           input_length=1, name='item_embedding',embeddings_regularizer=regularizers.l2(0.0001))(item_id_input)

user_vecs = Reshape([embedding_size])(user_embedding)
item_vecs = Reshape([embedding_size])(item_embedding)

y = Dot(1, normalize=False)([user_vecs, item_vecs])

model = Model(inputs=[user_id_input, item_id_input], outputs=y)

model.compile(loss='mse',
              optimizer="adam"
             )

import time
from keras.callbacks import ModelCheckpoint, EarlyStopping
mainpath = '.'
save_path = mainpath + "/models"
mytime = time.strftime("%Y_%m_%d_%H_%M")
modname = 'matrix_facto_30_' + mytime
thename = save_path + '/' + modname + '.h5'
mcheck = ModelCheckpoint(thename  , monitor='val_loss', save_best_only=True)
earlystop = EarlyStopping(monitor='val_loss', min_delta = 0.001, patience = 5, verbose = 1, mode='auto')
history = model.fit([data["User"],data["Anime"]],data["Rating"]
                    , batch_size=64, epochs=2
                    , validation_split=0.1
                    , callbacks=[mcheck,earlystop]
                    , shuffle=True)
#plot_model_history(history)
import pickle
with open(mainpath + '/histories/' + modname + '.pkl' , 'wb') as file_pi:
    pickle.dump(history.history, file_pi)