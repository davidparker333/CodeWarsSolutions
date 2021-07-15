# Write a program that prints the numbers from 1 to n and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”. For multiples of 3 and 5, print fizzbuzz

def fizzbuzz(n):
    for i in range(1, n):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(50)