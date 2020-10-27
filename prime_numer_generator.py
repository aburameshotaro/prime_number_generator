prime_factors = [2]
for i in range(3,100000,2):
    for j in prime_factors:
        if i%j==0:
            break
    else:
        prime_factors.append(i)
