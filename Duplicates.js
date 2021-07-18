//Write a function that prints any item in a list that is a duplicate

lis = [1,1,2,3,4,4,5,6,7,8,8]

let findDupes = (arr) => {
    let seen = {};
    let res = [];
    for (let i=0; i<arr.length; i++) {
        if (!(arr[i] in seen)) {
            seen[arr[i]] = 1;
        } else {
            seen[arr[i]]++;
        }
    }
    for (let ele in seen) {
        if (seen[ele] > 1) {
            res.push(ele);
        }
    }
    return res;
}

console.log(findDupes(lis));