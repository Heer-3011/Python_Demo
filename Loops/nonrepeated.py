dessert="Chocolate cake"

for char in dessert:
    dessert=dessert.lower()
    char_count=dessert.count(char)
    if char_count==1:
        print(char, "occurs only" ,char_count, "in the string")
        break