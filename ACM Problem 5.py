n = int(input('Enter a number: '))
a = []

for i in range(2, n//2 + 1):
    if n % i == 0:
        a.append(i)

prime = 0
for i in a:
    is_prime = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime = i

print(prime)
