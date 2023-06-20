// Write a function which calculates the average of the numbers in a given list.

// Note: Empty arrays should return 0.

function findAverage(array) {
  return array.length ? array.reduce((acc, x) => acc + x) / array.length : 0;
}
