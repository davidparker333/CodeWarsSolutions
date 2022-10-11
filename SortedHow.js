// Complete the method which accepts an array of integers, and returns one of the following:

// "yes, ascending" - if the numbers in the array are sorted in an ascending order
// "yes, descending" - if the numbers in the array are sorted in a descending order
// "no" - otherwise
// You can assume the array will always be valid, and there will always be one correct answer.

function isSortedAndHow(arr) {
  const sorted = [...arr].sort((a, b) => a - b);
  if (sorted.join() === arr.join()) {
    return "yes, ascending";
  } else if (sorted.reverse().join() === arr.join()) {
    return "yes, descending";
  }
  return "no";
}
