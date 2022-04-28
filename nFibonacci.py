# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).


def fibonacci(n: int) -> int:
    seq = [0, 1]
    while len(seq) <= n:
        seq.append(seq[-2]+seq[-1])
    return seq[n]


print(fibonacci(3))
