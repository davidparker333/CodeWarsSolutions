// Given the below array, add something to the beginning of the array, and add something to the end of the array

arr = [2,3,4,5];

// to the end
arr.push(6);

// to the beginning
arr.unshift(1);

//es6, beginning and end
arr = [0, ...arr, 7]

console.log(arr);

