// Given an array of n unsorted elements, write a function to search a given element x in array. Return its index. If it occurs more than once, return all indexes

let arr = [1,2,3,4,5,6,7,8,9,7]

let search = (arr, target) => {
    let res = [];
    for (let i=0; i<arr.length; i++) {
        if (arr[i] === target) {
            res.push(i);
        }
    }
    return res;
}

console.log(search(arr, 7));