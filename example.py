import json

file=open("example.json")
slownik=json.load(file)

file.close()
print(slownik)