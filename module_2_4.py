list_1 = [1, 2, 3, 8, 5, 11, 12, 13, 19, 23, 25, 81, 117, 97, 43, 47, 53, 59]
primes = []
not_primes = []
for i in list_1:
    if i < 2:
        not_primes.append(i)
    elif i%2 == 0 and i != 2:
        not_primes.append(i)
    elif i%3 == 0 and i != 3:
        not_primes.append(i)
    elif i%i**0.5 == 0:
        not_primes.append(i)
    else:
        primes.append(i)


print(primes)
print(not_primes)
