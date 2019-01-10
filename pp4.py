import json

with open("stat.json", "r") as readfile:
    data = json.load(readfile)


print(data)

for i in data:
    for j in i:
        print(j,':',i[j])

