import csv

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
        a = row[0]
        #print(a)
        if a not in tv_animes.keys():
            tv_animes[a] = len(tv_animes) + 1

with open('raw_data.csv', "r", encoding='utf-8') as raw_data:
    reader = csv.reader(raw_data, delimiter=',')
    for row in reader:
        u = row[0]
        a = row[1]
        rating = int(row[2])
        if rating !=0 and a in tv_animes.keys():
            if u not in users.keys():
                users[u] = len(users)+1
                rated[u] = {}
            if a not in animes.keys():
                animes[a] = len(animes)+1
            rated[u][a] = len(ratingList)
            ratingList.append((users[u], animes[a], rating))
with open('data.csv', "r", encoding='utf-8') as raw_data:
    reader = csv.reader(raw_data, delimiter=',')
    for row in reader:
        u= row[0]
        a = row[1]
        rating = int(row[2])
        if rating !=0 and a in tv_animes.keys():
            if u not in users.keys():
                users[u] = len(users)+1
                rated[u] = {}
            if a not in animes.keys():
                animes[a] = len(animes)+1
            if a not in rated[u].keys():
                ratingList.append((users[u], animes[a], rating))
            else:
                ratingList[rated[u][a]] = (users[u], animes[a], rating)
print("There are " + str(len(users)) + " number of users")
print("There are " + str(len(animes)) + " number of animes")
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
    for key, value in animes.items():
        csv_out.writerow([key.encode('utf-8'), value])
