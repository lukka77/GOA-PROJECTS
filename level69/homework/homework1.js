// 2) Even or Odd
let num = parseInt(prompt("Enter a number:"));
if (num % 2 === 0) {
  console.log("Even");
} else {
  console.log("Odd");
}

// 3) Grade Assignment
let score = parseInt(prompt("Enter score:"));
if (score >= 90) {
  console.log("Grade A");
} else if (score >= 80) {
  console.log("Grade B");
} else if (score >= 70) {
  console.log("Grade C");
} else if (score >= 60) {
  console.log("Grade D");
} else {
  console.log("Fail");
}

// 4) Largest of Three Numbers
let a = parseInt(prompt("Enter first number:"));
let b = parseInt(prompt("Enter second number:"));
let c = parseInt(prompt("Enter third number:"));

if (a === b && b === c) {
  console.log("All numbers are equal");
} else if (a >= b && a >= c) {
  console.log("Largest is: " + a);
} else if (b >= a && b >= c) {
  console.log("Largest is: " + b);
} else {
  console.log("Largest is: " + c);
}

// 5) Vowel or Consonant
let char = prompt("Enter a character:").toLowerCase();
if ("aeiou".includes(char)) {
  console.log("Vowel");
} else if (char >= 'a' && char <= 'z') {
  console.log("Consonant");
} else {
  console.log("Not a valid letter");
}

// 6) Divisible by 3 and 5
let number = parseInt(prompt("Enter a number:"));
if (number % 3 === 0 && number % 5 === 0) {
  console.log("Divisible by both");
} else if (number % 3 === 0) {
  console.log("Divisible by 3 only");
} else if (number % 5 === 0) {
  console.log("Divisible by 5 only");
} else {
  console.log("Not divisible by either");
}

// 7) Age Category
let age = parseInt(prompt("Enter age:"));
if (age >= 0 && age <= 12) {
  console.log("Child");
} else if (age <= 19) {
  console.log("Teenager");
} else if (age <= 59) {
  console.log("Adult");
} else {
  console.log("Senior");
}

// 8) Print 1 to 5 
let L = 1;
while (L <= 5) {
  console.log(i);
  i++;
}

// 9) Even Numbers from 2 to 10  
let i = 2;
while (i <= 10) {
  console.log(i);
  i += 2;
}

// 10) Print 10 to 1 
let S = 10;
while (S >= 1) {
  console.log(i);
  i--;
}

// 11) Print 1 to 10 
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// 12) First 5 Multiples of 3
for (let i = 1; i <= 5; i++) {
  console.log(i * 3);
}

// 13) Print 10 to 1 in Reverse 
for (let i = 10; i >= 1; i--) {
  console.log(i);
}

// 14) Even Numbers Between 1 and 20
for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}

// 15) Sum of Numbers from 1 to 5
let sum = 0;
for (let i = 1; i <= 5; i++) {
  sum += i;
}
console.log("Sum:", sum);