// Implement a bubble sort in JS

arr = [1,6,8,4,2,5,9,45,2,85,24,79,35,14];

let bubbleSort = (arr) => {
    isSorted = false;
    while (isSorted == false) {
        isSorted = true;
        for (let i=0; i<arr.length-1; i++) {
            if (arr[i] > arr[i+1]) {
                [arr[i], arr[i+1]] = [arr[i+1], arr[i]];
                isSorted = false;
            }
        }
    }
    return arr;
}

console.log(bubbleSort(arr))