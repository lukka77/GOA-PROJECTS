// საკლასო დავალება:
// Find the index of the first occurrence of "a" in the string "banana". Output the index of second occurence of "a".
// Check if the substring "world" exists in "Hello world" using indexOf.

const str = "banana";
console.log(str.indexOf("a"));
console.log(str.indexOf("a", 2));

const str2 = "Hello world";
console.log(str2.indexOf("world", 5))

// საკლასო დავალება:
// Replace the word "cat" with "dog" in the string "The cat is sleeping".
// Replace the first occurrence of "a" with "@" in "banana".
// Write a program to replace "world" with "JavaScript" in "Hello world".

const myStr = "The cat is sleeping";
console.log(myStr.replace("cat", "dog"));

const str5 = "banana";
console.log(str5.replaceAll("a", "@"));

const str7 = "Hello world";
console.log(str7.replace("world", "JavaScript"));


// საკლასო დავალება:
// Extract the word "world" from "Hello world" using slice.
// Get the first 5 characters from "JavaScript is fun" using slice.
// Use slice to remove the first character from "Python".

const sentence1 = "Hello world";
console.log(sentence1.slice(-5));

const word3 = "JavaScript is fun";
console.log(word3.slice(0, 5));

