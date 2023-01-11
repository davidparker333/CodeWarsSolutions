// Complete the function that takes a string of English-language text and returns the number of consonants in the string.

// Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

const consonantCount = (str) =>
  str.split("").filter((l) => l.match(/[b-df-hj-np-tv-z]/i)).length;
