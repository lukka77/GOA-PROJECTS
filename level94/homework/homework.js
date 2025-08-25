// 2-6)
// Use at() to get the first character of the string "JavaScript".
const word = "JavaScript";
console.log(word.at());

// Retrieve the last character of "OpenAI" using a negative index with at().
const word2 = "OpenAI";
console.log(word2.at(-1));

// Access the 5th character of the string "Programming" using at().
const word3 = "Programming";
console.log(word3.at(5));

// Write a function that returns the middle character of any given string using at().

// Use at() to get the second-to-last character of "Hello World".
const word4 = "Hello World";
console.log(word4.at(-2));

// 7-11)
// Concatenate "Hello" and "World" using concat() and print the result.
const word5 = "Hello";
const word6 = "World";
console.log(word5.concat(" ", word6));

// Use concat() to join three strings: "Good", " ", "Morning".
const word7 = "Good";
const word8 = " ";
const word9 = "Morning";
console.log(word7.concat(word8, word9));

// Concatenate a string and a number (converted to string) using concat().
let academy = "GOA"
console.log(academy.concat(10))

// Join a string with a special character, like "!" or "?", using concat().
console.log(academy.concat("!"))
console.log(academy.concat("?"))

// Concatenate a string with an empty string and observe the result.

// 12-16)

// Check if the string "Hello World" ends with "World".
const Str = "Hello world";
console.log(Str.endsWith("world"));

// Verify if the string "filename.pdf" ends with ".pdf".
const Str2 = "filename.pdf";
console.log(Str2.endsWith("pdf"));

// Use endsWith() to test whether "https://example.com/" ends with "/".
const URL = "https://example.com/";
console.log(URL.endsWith("/"))

// Write a function that returns true if a word ends with "s".

// Use the optional length parameter in endsWith() to check if "JavaScript" ends with "Java" considering only the first 4 characters.