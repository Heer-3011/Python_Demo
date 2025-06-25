roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for i in roll_number:
    if i in sample_dict:
        pass
    else:
        roll_number.pop(roll_number.index(i))

print(roll_number)