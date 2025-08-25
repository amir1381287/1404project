from re import search

# from  datetime import datetime
#
#
# text = input('enter text :\n ==>')
#
# now = str(datetime.now())
# now = now.split()
# now = now[1].split('.')
# print(now[0])
#
# alarm = input('enter your time :\n==>')
#
# print('ok  :-) wait\n')
# while True:
#     now = str(datetime.now())
#     now = now.split()
#     now = now[1].split('.')
#     if alarm ==  now[0] :
#       print(text)
#       break








# سلام استاد برا مرتب سازی و اینا میتونم از حلقه های تو در تو استفاده کنم که برنامه اصلا متوقف نشه ولی برا کم حجم شدن برنامه از اینکار منصرف شدم
# from dotenv import load_dotenv
# import os
# load_dotenv()
# PASSWORD_1 = os.getenv('PASSWORD')
# user_PASSWORD = input('enter password\n==>')
# if user_PASSWORD == PASSWORD_1 :
#     with open(file='book_store' , mode= 'r') as f :
#
#         all_book =[]
#         book_info = f.readlines()
#
#         for book in book_info :
#             book_dict = {}
#             book = book.strip()
#             book_data = book.split(',')
#             book_dict['book number'] = book_data[0]
#             book_dict['book name'] = book_data[1]
#             book_dict['book avthor'] = book_data[2]
#             book_dict['book genre'] = book_data[3]
#
#             all_book.append(book_dict)
#         print(all_book)
#         search_user = input('نام کتابی که دنبالشی را وارد کن:')
#
#         i = 0
#
#         while i != len(all_book):
#
#             a = dict(all_book[i])
#             b = a ['book name']
#
#             if b == search_user :
#                 print('موجود است')
#                 break
#
#             elif i == len(all_book)-1:
#                 print('موجود نیست')
#                 break
#
#             else:
#                 i +=1
#
#         dlete = input('کتابی که میخواید امانت ببرید را وارد کنید ')
#
#         while i != len(all_book):
#             a = dict(all_book[i])
#             b = a['book name']
#
#             if b == dlete:
#                 del all_book[i]
#                 break
#
#             else:
#                 i += 1
#         print(all_book)
#
#         book_dict_1 ={}
#
#         add_name = input('اسم کتاب باز گشتی رو وارد کنید:')
#
#         book_dict_1['book name'] = add_name
#
#         book_number = input('شماره کتابو وارد کنید:')
#
#         book_dict_1['book_number'] = book_number
#
#         book_avthor = input('نام نویسنده را وارد کنید:')
#
#         book_dict_1['book avthor'] = book_avthor
#
#         book_genre =input('ژانرو وارد کنید:')
#
#         book_dict_1['book_genre'] = book_genre
#
#         all_book.insert(int(book_number)-1 , book_dict_1)
#
#         print(all_book)
#
# else:
#     print('wrong')






for i in range(1 , 10) :

    for j in  range(1 , 10):
        #\t مثل سپیس است فاصله 
        print(f'{j} * {i} = {j * i}' , end='\t')
    print()





