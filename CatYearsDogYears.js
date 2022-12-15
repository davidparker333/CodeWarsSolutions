// I have a cat and a dog.

// I got them at the same time as kitten/puppy. That was humanYears years ago.

// Return their respective ages now as [humanYears,catYears,dogYears]

// NOTES:

// humanYears >= 1
// humanYears are whole numbers only
// Cat Years
// 15 cat years for first year
// +9 cat years for second year
// +4 cat years for each year after that
// Dog Years
// 15 dog years for first year
// +9 dog years for second year
// +5 dog years for each year after that

const humanYearsCatYearsDogYears = (humanYears) => {
  let dy = 0;
  let cy = 0;
  [...Array(humanYears).keys()].forEach((y) => {
    if (!y) {
      dy += 15;
      cy += 15;
    } else if (y === 1) {
      dy += 9;
      cy += 9;
    } else {
      dy += 5;
      cy += 4;
    }
  });
  return [humanYears, cy, dy];
};
