sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print( sampleDict['class']['student']['marks']['history'])

sampleDict["class"]['student']['name']='Heer'
print(sampleDict)