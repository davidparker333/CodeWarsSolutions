// Write a program that prints the numbers from 1 to n and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”. For multiples of 3 and 5, print fizzbuzz

let fizzBuzz = (n) => {
    for (let i=1; i<=n; i++) {
        if ((i % 3 == 0) & (i % 5 == 0)) {
            console.log("Fizzbuzz");
        } else if (i % 3 == 0) {
            console.log("Fizz");
        } else if (i % 5 == 0) {
            console.log("Buzz");
        }
    }
}

fizzBuzz(15);