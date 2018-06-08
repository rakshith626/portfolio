str=input("enter the string")

x=int(input("enter the starting number"))

y=int(input("enter the ending number"))

print(str[x:y])

​

enter the stringrakshithrk
enter the starting number3
enter the ending number9
hangad

a=[1,2,3,4,5]

flag=0

key=int(input("enter the  number"))

for i in range(0,5):

    if(

        key==a[i]):

        flag=1

        break

if flag:

     print("key element  is found" )

else:

    print("not found")