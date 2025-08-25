
my_list = {'amir','mohamad','ali'}

new_1 = 'n'

while new_1 =='n' :
    new_charecter = input('enter new name :\n')
    my_list.add(new_charecter)

    new_1 = input('new charecter enter n :\n')

start_whit = input('name start whit ?')

for start_1 in my_list :
    if start_1.startswith(start_whit):
        print(start_1)