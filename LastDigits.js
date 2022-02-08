// Your job is to implement a function which returns the last D digits of an integer N as a list.

// Special cases:
// If D > (the number of digits of N), return all the digits.
// If D <= 0, return an empty list.

lastDigit = (n, d) => {
  return d.length >= n.length
    ? n
    : d <= 0
    ? []
    : [...n.toString().slice(-d)].map((x) => parseInt(x));
};

console.log(lastDigit(123767, -4));
