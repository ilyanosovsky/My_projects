// Instructions
// Create a function that:

// takes in two strings as two parameters
// and returns a boolean that indicates whether or not the first 
// string is an anagram of the second string.

// Example of anagrams

// "Astronomer" is an anagram of "Moon starer"
// "School master" is an anagram of "The classroom"
// "The Morse Code" is an anagram of "Here come dots"

function anagram(str1, str2) {
    const str1Arr = str1.toLowerCase().replace(/\s/g,'').split("").sort().join('');
    const str2Arr = str2.toLowerCase().replace(/\s/g,'').split("").sort().join('');

    return str1Arr === str2Arr;

}

console.log(anagram("Astronomer", "Moon starer"));
console.log(anagram("School master", "The classroom"));
console.log(anagram("The Morse Code", "Here come dots"));