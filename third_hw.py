#1 = mojoudi
#2 = variz
#3 = bardasht
#4 khorouj

# mojoudi_hesab = 150000000
#
# operation = input('1 : mojoudi \n2 : variz\n3 : bardasht\n4 : khorouj\n==>')
#
# while operation != '4' :
#     if operation == '1' :
#         print(mojoudi_hesab)
#         pass
#
#
#     elif operation == '2':
#         account_number = input('شماره کارت مقصد را وارد کنید :\n==>')
#         amount = int(input('مبلغ را به ریال وارد کنید :\n ==>'))
#         if amount > mojoudi_hesab :
#             print('موجودی حساب شما کم است ')
#             pass
#         else :
#             mojoudi_hesab = mojoudi_hesab - amount
#             print(f"شماره کارت مقصد {account_number}\n"f"موجودی حساب شما : {mojoudi_hesab}\n"'تراکنش موفق')
#             pass
#     elif operation == '3' :
#         amount_1 = int(input('مبلغ برداشتی را وارد کنید :\n ==>'))
#         if amount_1 > 2000000 :
#             print('سقف برداشت در روز دویست هزار تومن است ')
#             pass
#         elif amount_1 > mojoudi_hesab :
#             print('موجودی حساب شما کم است ')
#             pass
#         else:
#             mojoudi_hesab = mojoudi_hesab - amount_1
#             print(f'تراکنش موفق\n موجودی حساب شما :{mojoudi_hesab}')
#             pass
#     else:
#         print('wrong')
#         pass
#
#     operation = input('1 : mojoudi \n2 : variz\n3 : bardasht\n4 : khorouj\n==>')





# part 2

my_text = """python is a high-level, general-purpose programming language.

Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically type-checked and garbage-collected.
It supports multiple programming paradigms, including structured (particularly

procedural), object-oriented and functional programming.

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC

programming language, and he first released it in 1991 as Python 0.9.0.

Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not
completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last
release of Python 2.

Python consistently ranks as one of the most popular programming languages, and it has

gained widespread use in the machine learning community."""

word_count = {}

for word in my_text.split():
   if word not in word_count :
       word_count[word] = 1
   else:
       word_count [word] += 1

word_1 = input('enter word :\n==>')
print(word_count[word_1])
print( len(my_text.split()))
print(word_count)







