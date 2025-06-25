keys=['One','Two','Three']
value=[10,20,30]
dictValue={}
for i in keys:
    for j in value:
        dictValue[i]=j

print(dictValue)

#using function 
res_dict = dict(zip(keys, value))
print(res_dict)