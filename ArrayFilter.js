// JavaScript Arrays support a filter function (starting in JavaScript 1.6). Use the filter functionality to complete the function given.

// The solution would work like the following:

// getEvenNumbers([2,4,5,6]) // should == [2,4,6]

const nums = [2, 3, 4, 5, 6, 7, 8, 9];

const getEvenNumbers = (numbersArray) => {
  return numbersArray.filter((num) => num % 2 !== 1);
};

console.log(getEvenNumbers(nums));
