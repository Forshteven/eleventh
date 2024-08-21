numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111, 12, 13, 14, 15, 49]
primes = []
not_primes = []
for i in numbers:
    if i < 4 and i != 1:
        primes.append(i)
    elif i % 2 ==0 or i % 3 ==0:
        not_primes.append(i)
    else:
        primes.append(i)
print(primes)
print(not_primes)

