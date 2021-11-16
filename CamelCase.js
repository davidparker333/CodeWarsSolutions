// Complete the method/function so that it converts dash/underscore delimited words into camel casing.
// The first word within the output should be capitalized only if the original word was capitalized
// (known as Upper Camel Case, also often referred to as Pascal case).

// Examples
var str1 = "the-stealth-warrior"; // gets converted to "theStealthWarrior"
var str2 = "The_Stealth_Warrior"; // gets converted to "TheStealthWarrior"
var str3 = "";

const toCamelCase = (str) => {
  if (str) {
    let resArr = str.indexOf("-") > 0 ? str.split("-") : str.split("_");
    if (resArr[0][0].toUpperCase() === resArr[0][0]) {
      for (let i = 0; i < resArr.length; i++) {
        resArr[i] = resArr[i].charAt(0).toUpperCase() + resArr[i].substr(1);
      }
    } else {
      for (let i = 0; i < resArr.length; i++) {
        if (i !== 0) {
          resArr[i] = resArr[i].charAt(0).toUpperCase() + resArr[i].substr(1);
        }
      }
    }
    return resArr.join("");
  }
  return str;
};

console.log(toCamelCase(str3));
