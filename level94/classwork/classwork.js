// საკლასო დავალება:
// Create two strings and use concat() to join them into one.
// Concatenate three strings together using concat().
// Use concat() to add a space between two words when joining them.
const myName = "Luka ";
const mySurname = "Gorgadze";
const str1 = "Batumi ";

console.log(myName.concat(mySurname));
console.log(str1.concat(mySurname, car));
console.log(myName.concat("", car));


// საკლასო დავალება:
// Use endsWith() to test whether a URL ends with "/".
// Write a function that checks if a given word ends with the letter "s".

const myStr = "Hello world!, GOA academy."
console.log(myStr.endsWith("/")); // false

const cw = s => {
    return s.endsWith("s")
}
console.log(cw("class"))


// საკლასო დავალება:
// Write a function that returns true if a sentence ends with punctuation (".", "?", or "!").

const CheckEnding = sentence => {
    return sentence.endsWith(".") || sentence.endsWith("?") || sentence.endsWith("!")
}

console.log(CheckEnding("gmepmgpier."))
console.log(CheckEnding("gmepmgpier?"))
console.log(CheckEnding("gmepmgpier!"))
console.log(CheckEnding("gmepmgpier"))