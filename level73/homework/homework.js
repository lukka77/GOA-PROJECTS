// 2) Create a new <p> and add it to the body
let newPara = document.createElement("p");
newPara.textContent = "This is a new paragraph.";
document.body.appendChild(newPara);

// 3) Create an <h1> and append it to a <div>
let heading = document.createElement("h1");
heading.textContent = "Hello from h1!";
document.getElementById("myDiv").appendChild(heading);

// 4) Create an <img> and add it to the page
let img = document.createElement("img");
img.src = "https://www.youtube.com/@Goal_Oriented_Academy__GOA/videos";
img.alt = "Sample Image";
document.body.appendChild(img);

// 5) Create a <button> with text "Click me" and add to body
let btn = document.createElement("button");
btn.textContent = "Click me";
document.body.appendChild(btn);

// 6) Create a <ul> and add 3 <li> items
let ul = document.createElement("ul");
["Item 1", "Item 2", "Item 3"].forEach(text => {
  let li = document.createElement("li");
  li.textContent = text;
  ul.appendChild(li);
});
document.body.appendChild(ul);

// 7) Remove first child from <div id="content">
let contentDiv = document.getElementById("content");
if (contentDiv.firstElementChild) {
  contentDiv.removeChild(contentDiv.firstElementChild);
}

// 8) Create new <ul> with 3 <li>, then remove last <li>
let ul2 = document.createElement("ul");
["A", "B", "C"].forEach(text => {
  let li = document.createElement("li");
  li.textContent = text;
  ul2.appendChild(li);
});
document.body.appendChild(ul2);
ul2.removeChild(ul2.lastElementChild);

// 9) Replace <p> inside #textContainer
let newP = document.createElement("p");
newP.textContent = "I am a new paragraph!";
let container = document.getElementById("textContainer");
let oldP = document.getElementById("oldPara");
container.replaceChild(newP, oldP);

// 10) Replace <button> with <span> inside #buttonContainer
let newSpan = document.createElement("span");
newSpan.textContent = "I replaced the button!";
let buttonContainer = document.getElementById("buttonContainer");
let oldButton = document.getElementById("oldButton");
buttonContainer.replaceChild(newSpan, oldButton);

// 11) Replace <li> inside #singleList with a new <li>
let newLi = document.createElement("li");
newLi.textContent = "New list item!";
let list = document.getElementById("singleList");
let oldLi = list.firstElementChild;
list.re
