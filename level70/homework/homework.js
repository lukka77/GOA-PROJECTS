// 1) Print numbers from 1 to 10 using for loop
printLine("Numbers from 1 to 10 (for loop):");
for(let i=1; i<=10; i++) {
  printLine(i);
}

// 2) Print even numbers from 2 to 20 using while loop
printLine("\nEven numbers from 2 to 20 (while loop):");
let j = 2;
while(j <= 20) {
  printLine(j);
  j += 2;
}

// 3) Print numbers from 10 down to 1 using for loop
printLine("\nNumbers from 10 down to 1 (for loop):");
for(let k = 10; k >= 1; k--) {
  printLine(k);
}

// 4) Print first 5 multiples of 3 using while loop
printLine("\nFirst 5 multiples of 3 (while loop):");
let count = 1;
while(count <= 5) {
  printLine(count * 3);
  count++;
}

// 5) Print each character of a string using for loop
let sampleString = "Hello!";
printLine(`\nCharacters in string "${sampleString}":`);
for(let idx=0; idx < sampleString.length; idx++) {
  printLine(sampleString[idx]);
}

// Button events
document.getElementById("changeTextBtn").addEventListener("click", () => {
  document.getElementById("paragraph").textContent = "Paragraph text has been changed!";
});

document.getElementById("changeBgBtn").addEventListener("click", () => {
  document.getElementById("colorDiv").style.backgroundColor = "orange";
});

document.getElementById("changeFontBtn").addEventListener("click", () => {
  document.getElementById("heading").style.fontSize = "40px";
});

document.getElementById("hideDivBtn").addEventListener("click", () => {
  document.getElementById("hideDiv").style.display = "none";
});

document.getElementById("alertBtn").addEventListener("click", () => {
  alert("This is a custom alert message!");
});
