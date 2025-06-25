sampleDict = { 
  "name": "Heer",
  "age":20, 
  "salary": 10000, 
  "city": "Ahemdabad" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

#delte list of keys from dictionary 
sampleDict = { 
  "name": "Heer",
  "age":20, 
  "salary": 10000, 
  "city": "Ahemdabad" }

keys = ["name", "salary"]
for k in keys:
    sampleDict.pop(k)
print(sampleDict)
