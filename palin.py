#PALINDROME

Num = int(input("Please Enter any Number: "))

i = 0

temp=Num

while(Num > 0):

 j = Num %10

 i= (i *10) + j

 Num = Num //10

if (temp==i):

  print("number is palindrome")

else:

    print("number is not a palindrome")
