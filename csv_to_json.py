import csv
import json

anime_list = {}
with open('./data/anime_id.csv', "r", encoding='utf-8') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        anime_list[row[0][2:-1]] = row[1]


with open('anime_id.json',"w") as file:
    json.dump(anime_list,file)