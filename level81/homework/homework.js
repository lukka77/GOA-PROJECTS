// 4-8)
// Print numbers from 1 to 5 using a do...while loop.
let result = "";
let i = 0;

do {
    i +=1;
    result += i;
} while (i < 5);

console.log(result)

// Print even numbers from 2 to 10 using a do...while loop.
// Print the numbers from 10 down to 1 using a do...while loop.
// Ask the user to enter a number until they enter a number greater than 100.
let ul = document.getElementById("ul-main");
letnumberSum = 0;

do {
    let userNumber = Number(prompt("Enter number: "));
    numberSum += userNumber;

    let newLi = document.createElement("li");
    newLi.textContent = numberSum;
    ul.appendChild(newLi)
} while (numberSum <= 100);

// Sum numbers from 1 to 10 and print the total using a do...while loop.


// 9-13)
// Use a for...of loop to print each element of an array of numbers.
const array1 = ["a", "b", "c"]

for (const element of array1) {
    console.log(element);
}
// Use a for...of loop to print each character of a string. 
function logChars(myStr) {
    for (let char of myStr){
        console.log(char)
    }
}

logChars("Hello world!")
// Use a for...of loop to sum all numbers in an array and print the total.
function sumNumbers(myArr){
    let sum = 0;

    for (const num of myArr){
        sum += num;
    }
    return sum;
}

console.log(sumNumbers([2, 4, 6, 4, 1, 4]))
// Use a for...of loop to print only the even numbers from an array of numbers.
// Use a for...of loop to print all names from an array of names.


// 14-18)
// Use a for...in loop to print all property names (keys) of an object.
let myObj = {
    name: "Luka",
    surname: "Gorgadze",
    age: 15,
    city: "Batumi"
}

for (let გასაღები in myObj){
    console.log(გასაღები )
}

// Use a for...in loop to print all property values of an object.
let myobj = {
    name: "Nika",
    surname: "Beridze",
    Number: 20,
    city: "Tbilisi"
}

for (let გასაღები in myobj){
    console.log("გასაღები არის:", გასაღები, "ხოლო ამ გასაღების მნიშვნელობა არის:", myobj[გასაღები])
}
// Use a for...in loop to count the number of properties in an object.
// Use a for...in loop to check if a specific key exists in an object.
// Use a for...in loop to create a string listing all keys from an object.