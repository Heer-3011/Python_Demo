str1="Make a lot money"
str2="But now"
str3="Subscribe this"
str4="Click this"

str_list=[str1,str2,str3,str4]
print(str_list)

str=input("enter string")
for i in str_list:
    if i.lower()==str.lower(): 
        print("Spam")
    else:
        print("not spamm")
        break