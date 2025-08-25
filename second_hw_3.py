

name_number =input('enter name :\n==>')
number = ''
for number_1 in name_number :
    if  number_1.isdigit():
        number += number_1

print(f'number is : {int(number)}')