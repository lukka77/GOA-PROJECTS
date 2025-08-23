// 2-6)
// Check if the word "dog" exists in "The quick brown fox jumps over the lazy dog".
console.log("The quick brown fox jumps over the lazy dog".includes("dog"));

// Write a function that returns true if a string contains "@" (basic email check).
function isEmail(str) {
    return str.includes("@");
}

console.log(isEmail("1234@gmail.com"));
console.log(isEmail("GOA.com"));

// Use includes to see if "Java" exists in "JavaScript".
console.log("JavaScript".includes("Java"));

// Check if "apple" exists in "pineapple".
console.log("pineapple".includes("apple"));

// Write a function that checks if a sentence contains the word "not".
function contains(sentence){
    return sentence.includes("not");
}

console.log(contains("This is not good"));
console.log(contains("This is great"));


// 7-11)
// Find the index of "fox" in the string "The quick brown fox jumps over the lazy dog".
const str = "The quick brown fox jumps over the lazy dog";
console.log(str.indexOf("fox"));

// Write a program that returns the index of the first "o" in "Hello world".
const word = "Hello world";
console.log(word.indexOf("o"))

// Use indexOf to find the position of "2025" in "Happy New Year 2025!".
const find2025 = "Happy New Year 2025!";
console.log(find2025.indexOf("2025"));

// Find the index of "is" in "This is a simple test".
const test = "This is a simple test";
console.log(test.indexOf("is"));

// Write a function that checks if "@" exists in a string and returns its index, or -1 if not found.
function findASymbol(str){
    return str.indexOf("@");
}

console.log(findASymbol("12345@gmail.com"));


// 12-16)
// Find the last index of "o" in the string "Hello world".
const findLastIndex = "Hello world";
console.log(findLastIndex.lastIndexOf("o"))

// Write a program that returns the last index of "a" in "banana".
const word2 = "banana";
console.log(word2.lastIndexOf("a"));

// Use lastIndexOf to find the position of the last "is" in "This is a test, and it is simple".
const word3 = "This s a test, and it is simple";
console.log(word3.lastIndexOf("is"));

// Check the last index of "dog" in "dog dog dog".
const word4 = "dog dog dog";
console.log(word4.lastIndexOf("dog"));

// Find the last index of "2025" in "Happy 2025, welcome 2025!".
const word5 = "Happy 2025, welcome 2025!";
console.log(word5.lastIndexOf("2025"));


// 17-21)
// Repeat the string "ha" 3 times to make "hahaha".
const word6 = "ha";
console.log(word6.repeat(3));

// Write a program that repeats "*" 10 times to create a line of stars.
const word7 = "*";
console.log(word7.repeat(10));

// Use repeat to create a dashed line "---" repeated 5 times.
const line = "---";
console.log(line.repeat("5"));

// Write a function that takes a word and repeats it n times.
function repeatWord(word, n){
    return word.repeat(n);
}
console.log(repeatWord("Hello", 5));

// Create a string that repeats "Hello " 4 times.
const createStr = "Hello".repeat(4);
console.log(createStr);


// 22-26)
// Replace the first occurrence of "cat" with "dog" in "The cat chased the cat".
const word8 = "The cat chased the cat";
console.log(word8.replace("cat", "dog"));

// Replace "Java" with "Type" in "JavaScript is cool".
const word9 = "JavaScript is cool";
console.log(word9.replace("Java", "Type"));

// Write a function that replaces the first space " " in a sentence with a hyphen "-".
function replace1(sentence){
    return sentence.replace(" ", "-");
}
console.log(replace1("Hello world"));

// Replace the first "a" with "@" in "banana".
const word10 = "banana";
console.log(word10.replace("a", "@"));

// Change "2024" to "2025" in "Happy New Year 2024!".
const word11 = "Happy New Year 2024!";
console.log(word11.replace("2024", "2025"));


// 27-31)
// Replace all "cat" with "dog" in "The cat chased another cat and found a cat".
const word12 = "The cat chased another cat and found a cat";
console.log(word12.replaceAll("cat", "dog"));

// Replace all spaces " " with hyphens "-" in "I love JavaScript so much".
const word13 = "I love JavaScript so much";
console.log(word13.replaceAll(" ", "-"));

// Replace all "a" with "@" in "banana".
const word14 = "banana";
console.log(word14.replaceAll("a", "@"));

// Change all "2024" to "2025" in "2024 was great, but 2024 is over".
const word15 = "2024 was great, but 2024 is over";
console.log(word15.replaceAll("2024", "2025"));

// Replace all "." with "!" in "Wait. Stop. Go. Run.".
const word16 = "Wait. Stop. Go. Run";
console.log(word16.replaceAll(".", "!"));


// 32-36)
// Extract "world" from "Hello world" using slice.
const word17 = "Hello world";
console.log(word17.slice(-5));

// Get the first 4 characters from "JavaScript" using slice.
const word18 = "JavaScript";
console.log(word18.slice(-6));

// Remove the first character from "Python" using slice.
const word19 = "Python";
console.log(word19.slice(1));

// Extract the last 3 characters from "Banana" using slice.
const word20 = "Banana";
console.log(word20.slice(0, 3));

// Write a function that returns the first half of any given string using slice.
function firstHalf(str) {
  const halfLength = Math.floor(str.length / 2);
  return str.slice(0, halfLength);
}
console.log(firstHalf("hello"));