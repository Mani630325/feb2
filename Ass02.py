a=-1

b=1

n=int(input('enter n value:'))

sum=0

for i in range(1,n+1):

    c=a+b

    print(c)

    sum=sum+c

    a=b

    b=c

    

print('sum of n number of febnocci seriesi:',sum)
