// Print the first 15 digits of the fibonacci sequence

let fib = (n) => {
    let fibList = [0,1];
    for (let i=2; i<n; i++) {
        fibList.push(fibList[i-1] + fibList[i-2])
    }
    return fibList
}

console.log(fib(15));