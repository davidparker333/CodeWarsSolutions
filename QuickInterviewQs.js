// Write a function that remove odd numbers from an array of numbers

arr = [1,2,3,4,5,6,7,8,9];

let removeOdd = (arr) => {
    return arr.filter(num => num % 2 == 0);
}


// Return an array of its values plus the values index

let addIndex = (arr) => {
    let res = [];
    for (let i=0; i<arr.length; i++) {
        res.push(i + arr[i]);
    }
    return res;
}

console.log(addIndex(arr));


