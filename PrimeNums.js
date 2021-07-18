//Print the prime numbers between 100 and 200

let primeNums = () => {
    var isPrime;
    for (let i=100; i<201; i++) {
        isPrime = true;
        for (let j=2; j<i; j++) {
            if (i % j === 0) {
                isPrime = false;
            }
        }
        if (isPrime) {
            console.log(i);
        }
    }
}

primeNums();