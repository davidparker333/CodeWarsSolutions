// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

function moveZeros(arr) {
  let count = 0;
  for (const num of arr) {
    if (num === 0) {
      count++;
    }
  }
  const filtered = arr.filter((e) => e !== 0);
  for (let i = 0; i < count; i++) {
    filtered.push(0);
  }
  return filtered;
}
