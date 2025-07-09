// 2
let count = 1;
let interval1 = setInterval(() => {
  console.log(count);
  count++;
  if (count > 5) {
    clearInterval(interval1);
  }
}, 1000);

// 3
let interval2 = setInterval(() => {
  console.log("This message shows every 2 seconds");
}, 2000);

setTimeout(() => {
  clearInterval(interval2);
}, 10000);

// 4
let changeCount = 0;
let colors = ["lightblue", "lightgreen", "lightcoral", "lightpink", "lightyellow"];
let interval3 = setInterval(() => {
  document.body.style.backgroundColor = colors[changeCount % colors.length];
  changeCount++;
  if (changeCount >= 5) {
    clearInterval(interval3);
  }
}, 3000);

// 5
let timeInterval = setInterval(() => {
  let now = new Date();
  console.log("Current Time:", now.toLocaleTimeString());
}, 1000);

setTimeout(() => {
  clearInterval(timeInterval);
}, 15000);

// 6)
let seconds = 0;
let timer = setInterval(() => {
  console.log("Timer:", seconds + "s");
  seconds++;
  if (seconds > 10) {
    clearInterval(timer);
  }
}, 1000);

// 7
let numbers = [10, 20, 30, 40];
console.log("Second element:", numbers[1]);

// 8
numbers[0] = 100;
console.log("Updated array:", numbers);

// 9
let fruits = ["apple", "banana", "cherry"];
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);

// 10
let nums = [5, 10, 15, 20, 25];
let sum = nums[0] + nums[nums.length - 1];
console.log("Sum of first and last:", sum); 
