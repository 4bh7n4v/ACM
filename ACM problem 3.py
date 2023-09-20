a=int(input("enter number"))
q = a//3
w = a//5
count = 1
sum = 0
if(q*3==a):
    while(count < q-1):
        count = 1
        x=3*count
        sum = sum + x
        count = count + 1
else:
    count = 1
    while(count <= q):
        x=3*count
        sum = sum + x
        count = count + 1
count = 1
if(w*5==a):
    while(count < w):
       y = 5*count
       sum = sum + y
       count = count + 1 
else:
    count = 1
    while(count <= w):
        count = 1
        y=5*count
        sum = sum + y
        count = count + 1
print('sum of multiple of 3,5=',sum)