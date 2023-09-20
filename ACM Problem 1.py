n=int(input('no of test cases'))
count = 0
sum = 0
while(count < n):
    r=int(input('enter a number'))
    if(r%2!=0):
        sum += r
    else:
        print("even not include in sum")
    count += 1 
print(sum)