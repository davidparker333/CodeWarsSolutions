// Given a string as your inputs, delete any recorruring character

let s = "This is a sentence with some reoccuring characters in it";

let removeReoccuring = (s) => {
    let seen = [];
    let res = "";
    for (let i=0; i<s.length; i++) {
        if (!(seen.includes(s[i]))) {
            res = res + s[i];
            seen.push(s[i]);
        }
    }
    return res;
}

console.log(removeReoccuring(s));