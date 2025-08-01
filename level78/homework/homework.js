// 2
const paragraphs = document.querySelectorAll("p");
alert("პარაგრაფების რაოდენობა: " + paragraphs.length);

// 3
const h2Elements = document.querySelectorAll("h2");
h2Elements.forEach(h2 => {
  h2.style.color = "blue";
});

// 4
const listItems = document.querySelectorAll("li");
listItems.forEach(li => {
  console.log(li.textContent);
});

// 5
const divs = document.querySelectorAll("div");
divs.forEach(div => {
  div.style.backgroundColor = "lightgray";
});

// 6
const firstImage = document.querySelector("img");
firstImage.src = "https://via.placeholder.com/150";


// 7
const highlights = document.querySelectorAll(".highlight");
highlights.forEach(el => {
  el.style.backgroundColor = "yellow";
});

// 8
const cards = document.querySelectorAll(".card");
console.log("კარდების რაოდენობა: " + cards.length);

// 9
const errors = document.querySelectorAll(".error");
errors.forEach(el => {
  el.style.color = "red";
});

// 10
const items = document.querySelectorAll(".item");
items.forEach(el => {
  console.log(el.innerHTML);
});

// 11
const button = document.querySelector(".button");
button.textContent = "Clicked!";

// 12
  const div = document.getElementById("movingDiv");
  let left = 0;
  const move = setInterval(() => {
    left += 5;
    div.style.left = left + "px";
  }, 100);