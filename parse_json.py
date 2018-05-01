import json
import csv

with open('raw_data.json', "r", encoding='utf-8') as data:
    j = json.load(data)
users = {}
anime = {}
ratingList = []
for u in j:
    if u not in users.keys():
        users[u] = len(users)+1
    for a in j[u]:
        if a not in anime.keys():
            anime[a] = len(anime)+1
        ratingList.append((users[u], anime[a], j[u][a]))
print(len(users))
with open("data/ratings.csv", "w", encoding='utf-8', newline='') as file:
    csv_out = csv.writer(file)
    for row in ratingList:
        csv_out.writerow(row)
    file.close()
with open("data/user_id.csv", "w", encoding='utf-8', newline='') as file:
    csv_out = csv.writer(file, delimiter="\t")
    for key, value in users.items():
        csv_out.writerow([key.encode('utf-8'), value])
with open("data/anime_id.csv", "w", encoding='utf-8', newline='') as file:
    csv_out = csv.writer(file, delimiter="\t")
    for key, value in anime.items():
        csv_out.writerow([key.encode('utf-8'), value])
