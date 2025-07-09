let fruits = ["apple", "banana", "orange", "mango", "pineapple"];

console.log("First fruit:", fruits[0]);
console.log("Last fruit:", fruits[fruits.length - 1]);

console.log("Total fruits:", fruits.length);
console.log("Final array:", fruits);


// 2
let colors = ["red", "green", "blue"];
colors.push("yellow");
colors.shift();
colors.unshift("purple");
console.log("Modified colors array:", colors);

// 3
let numbers = [2, 3, 4];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i] * 2);
}

// 4
function sumArray(arr) {
  let sum = 0;
  for (let num of arr) {
    sum += num;
  }
  return sum;
}
console.log("Sum of [1, 2, 3]:", sumArray([1, 2, 3])); 

// 5
function findLargest(arr) {
  if (arr.length === 0) return null;

  let largest = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  return largest;
}
console.log("Largest number:", findLargest([5, 10, 3, 8, 2]));