// Write a function to check if a string is palindrome or not

let palindrome = (s) => {
    if (s.toLowerCase().split("").reverse().join("").replaceAll(" ", "") === s.toLowerCase().replaceAll(" ", "")) {
        return true;
    } else {
        return false;
    }
}

console.log(palindrome("Racecar"));

console.log(palindrome("Murder for a jar of red rum"));