// Write a function that when called returns another function. The outer function will take in x. The inner function will take in y. Upon calling the inner function, x and y will be added

let closure = (x) => {
    return innerClosure = (y) => {
        return x + y;
    }
}

let add10 = closure(10);

console.log(add10(5));