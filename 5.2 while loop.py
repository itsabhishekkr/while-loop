#prime number   D0UBT
"""""""""n=int(input("enter no"))
i=2
a=False
while(i<(n-1)):
    if(n%i==0):
        i=i+1
        print(i)
        a=True
if(a==True):
    print(" NOT prime")
else:
    print(" prime")   """""""""        