import logging

from logging import log
logging.basicConfig(filename='file.log', level= 0)
logger = logging.getLogger()
#
# f = open('txt.intelligence_artificial' ,  'r', encoding='utf-8' )
#
# list_1 = []
#
# i = f.read()
# i = i.split()
#
# for r in i :
#     if r.isdigit() :
#         logger.log(msg= 'Separation numbers' , level= 20)
#
#         list_1.append(r)
# print(list_1)





# def Earth_gravity (high : float , mass :float) ->float :
#     gravity = 9.8
#     u = mass * gravity * high
#     return u
#
# high = float(input('enter high :\n==>'))
# mass = float(input('enter mass:\n==>'))
# earth_gravity = Earth_gravity(high , mass)
# logger.log(msg='Substitution numbers' , level= 20)
# print(earth_gravity)




for number , i in enumerate (range( 1 , 101 ),start= 1):
    logger.log(msg= f'create file {number}' , level=20 )
    f = open(f'amir/file{number}.txt' , 'w')