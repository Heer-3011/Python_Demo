speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 
         'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
list1=[]
for i in speed.values():
    if i in list1:
        pass
    else:
        list1.append(i)

print(list1)