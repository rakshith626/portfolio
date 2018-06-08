#lucky seven

import random

user=int(input("enter the number"))

com=random.randint(1,7)

if(com>user):

   print("your input is less than ran num")

elif(com<user):

   print("your input is greater than ran num")

else:

   print("you won the game")

    