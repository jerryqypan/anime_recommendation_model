import csv
import json
users = {}
tv_animes = {}
ratingList = []
rated = {}
animes = {}

# with open('raw_data.csv', "r", encoding='utf-16') as raw_data:
#     reader = csv.reader(raw_data, delimiter=',')
#     for row in reader:
#         u = row[0]
#         a = row[1]
#         r = int(row[2])
#         print(u,a,r)
with open('tvseries.csv', "r", encoding='latin-1') as wanted_anime:
    reader = csv.reader(wanted_anime, delimiter=',')
    for row in reader:
        name = row[0]
        link = row[4]
        genre = row[3]
        tv_animes[name] = {}
        tv_animes[name]["image_url"] = link
        tv_animes[name]["genre"] = genre
with open('tv_images.json',"w",encoding='latin-1') as file:
    json.dump(tv_animes,file)



