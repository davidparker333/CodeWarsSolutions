#Print the first 15 digits of the fibonacci sequence

def find_fib(n):
    fib = [0,1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(find_fib(15))