// Print numbers from 1 to 20, but stop the loop if the number is 13.
for(let number = 0; number <= 20; number++){
    if(number == 13){
        continue
    }
    console.log(number)
}

// Loop through an array of colors and stop when you find "blue".
const coloursArr = ["red", "green", "blue", "purple", "black"]
for (colour of coloursArr){
    if(color == "blue"){
        continue
    }
    console.log(colour)
}

// Count from 1 to 50, but stop when the number is divisible by both 4 and 5.
for(let number = 1; number <= 50; number++){
    if(number %4 == 0 && number %5 == 0){
        continue
    }
    console.log(number)
}

// Print each letter in a word, and stop when the letter is "a".
let word = "GOA is the best academy"
for(letter of word){
    if(letter == "a"){
        continue
    }
    console.log(letter)
}

// Keep adding numbers from 1 upwards, and stop when the total sum reaches 100.
let sum = 1

for(let i = 0; i <= 100; i++){
    if(sum >= 100){
        break
    }
    console.log(sum)
    sum += i
}

// Print numbers from 1 to 20, but skip (don’t print) the number 13.
for(let i = 1; i <= 20; i++){
    if(i == 14){
        break
    }
    console.log(i)
}

// Loop through an array of fruits and skip printing "banana".
let fruits = ["apple", "pinneaple", "banan", "orange"]
for(let i = 0; i < fruits.length; i++){
    if(fruits[i] == "banan"){
        break
    }
    console.log(fruits[i])
}

// Count from 1 to 30, but skip numbers that are divisible by 3.
for(let number = 1; number <= 30; number++){
    if(number % 3 == 0){
        break
    }
    console.log(number)
}

// Print each letter in a word, but skip the letter "e".
let word1 = "moile phone"

for(letter of word1){
    if(letter == "e"){
        break
    }
    console.log(letter)
}

// Loop through numbers from 1 to 50, and skip all even numbers.
for(let i = 0; i <= 50; i++){
    if(i % 2 != 0){
        continue
    }
    console.log(i)
}

// Create an arrow function that adds two numbers and returns the result.
const arrowFunc1 = (num1, num2) => {
    console.log(num1 + num2)
}
arrowFunc1(5,7)

// Write an arrow function that takes a name and returns a greeting message like "Hello, John!".
const arrowFunc2 = (name) => {
    console.log("Hello", name)
}
arrowFunc2("luka")

// Make an arrow function that takes an array of numbers and returns a new array with each number doubled.
const doubledNums = (arr) => {
    let newArr = []
    for(num of arr){
        newArr.push(num * 2)
    }
    console.log(newArr)
}

doubledNums([1,2,3,4,5])

// Create an arrow function that checks if a number is even and returns true or false.
const isEven = () => {
    if(num %2 == 0){
        console.log(true)
    }else{
        console.log(false)
    }
}

isEven(50)

// Write an arrow function that takes a string and returns its length.
const arrowFunc3 = (str) => {
    console.log(str.lenght)
}
arrowFunc3("GOA")