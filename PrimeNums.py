#Print the prime numbers between 100 and 200

def print_primes():
    result = []
    for i in range(100, 201):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime == False:
            continue
        else:
            result.append(i)
    return result

print(print_primes())