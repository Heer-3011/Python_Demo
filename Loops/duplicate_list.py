list1=['apple','banana','kiwi','kiwi','mango']

for word in list1:
    count=list1.count(word)
    if count>1:
        print("Dupicate found",word)
        break