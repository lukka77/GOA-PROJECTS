// 1. Countdown Timer:
// Create a countdown from 10 to 0 using setInterval. Log each number every second. 
// When it reaches 0, stop the interval and log "Time's up!".
let count = 10;
const timer = setInterval(() => {
  console.log(count);
  count--;
  if (count < 0) {
    clearInterval(timer);
    console.log("Time's up!");
  }
}, 1000);


// 2. Flashing Title:
// Change the document.title between "Hello" and "Goodbye" every 1 second. After 6 seconds, stop the interval.
let toggle = true;
const flash = setInterval(() => {
  document.title = toggle ? "Hello" : "Goodbye";
  toggle = !toggle;
}, 1000);

setTimeout(() => clearInterval(flash), 6000);

// 3. Move a Box (Optional DOM Task):
// Create a box (div) and move it 10px to the right every 200ms using setInterval. Stop after it moves 100px.
  let position = 0;
  const box = document.getElementById("box");
  const move = setInterval(() => {
    if (position >= 100) {
      clearInterval(move);
    } else {
      position += 10;
      box.style.left = position + "px";
    }
  }, 200);


// 4. Random Number Logger:
// Log a random number between 1 and 10 every 1.5 seconds. Stop it after 5 numbers are logged.
let countRandoms = 0;
const randomLogger = setInterval(() => {
  const num = Math.floor(Math.random() * 10) + 1;
  console.log(num);
  countRandoms++;
  if (countRandoms === 5) {
    clearInterval(randomLogger);
  }
}, 1500);



// 5. Array to Uppercase:
// Create an array of 3 lowercase strings. Use a loop to convert each to uppercase and log them.
const words = ["apple", "banana", "cherry"];
for (let i = 0; i < words.length; i++) {
  console.log(words[i].toUpperCase());
}


// 6. Replace Middle Element:
// Create an array of 3 numbers. Replace the middle number with 0. Log the array.
const nums = [1, 2, 3];
nums[1] = 0;
console.log(nums);


// 7. Add and Remove Elements:
// Create an array with 2 elements. Add one element to the end and one to the beginning. Then remove the last one. Log the final array.
let items = ["first", "second"];
items.push("third"); 
items.unshift("zero"); 
items.pop();
console.log(items);


// 8. Average of Array:
// Create an array of 4 numbers. Calculate and log the average.
const values = [4, 8, 6, 2];
let sum = 0;
for (let val of values) {
  sum += val;
}
console.log("Average:", sum / values.length); 


// 9. Reverse an Array Manually:
// Create an array of 3 elements and manually (not using .reverse()) log the elements in reverse order using indexing.
const arr = ["a", "b", "c"];
console.log(arr[2]);
console.log(arr[1]);
console.log(arr[0]);


// 10. Loop with Index:
// Create an array of any 5 elements. Use a for loop to log each value and its index like this:
// python-repl
// Copy
// Edit
// Index 0: apple  
// Index 1: banana  
// ...
const fruits = ["apple", "banana", "orange", "pineapple", "carrot"];

for (let i = 0; i < fruits.length; i++) {
  console.log("index " + i + ": " + fruits[i]);
}