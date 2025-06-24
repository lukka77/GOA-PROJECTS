// 1) 
let person = {
  name: "Luka",
  age: 15,
  city: "Batumi"
};

// 2) 
console.log("Name:", person.name);

// 3) 
person.country = "USA";
console.log("After adding country:", person);

// 4)
let employee = {
  id: 1,
  details: {
    name: "John",
    department: "Engineering"
  }
};
console.log("Employee department:", employee.details.department);

// 5) 
person.city = "Los Angeles";
console.log("Updated city:", person.city);

let num1 = 15;
let num2 = 20;

// 6) 
console.log(num1 > 10 && num2 > 10); 

// 7)
console.log(num1 > 10 || num2 < 5); 

// 8) 
let isAvailable = true;
console.log("Not available:", !isAvailable); 

// 9) 
let x = 12;
let y = 5;
let z = false;

let result = (x > 10 && y < 10) || !z;
console.log("Combined logic result:", result); 

// 10) 
let num = 42;
let numStr = String(num);
console.log("String:", numStr, typeof numStr); 

// 11) 
let boolVal = true;
let boolStr = String(boolVal);
console.log("Boolean as string:", boolStr, typeof boolStr);

// 12) 
let strNum = "123";
let convertedNum = Number(strNum);
console.log("Converted number:", convertedNum, typeof convertedNum);

// 13) 
console.log(Number(true)); 
console.log(Number(false));

// 14) 
let nonNumeric = "hello";
let converted = Number(nonNumeric);
console.log("Converted non-numeric string:", converted);

