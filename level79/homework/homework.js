// ✅ Homework 2: Paragraph Word Counter
// Select all <p> tags.
// For each <p>, count how many words it contains.
// Log each count in the console like:
// Paragraph 1 has 14 words, Paragraph 2 has 5 words...

let Paragraph = document.getElementsByTagName("p")
for (let i = 0; i < Paragraph.length; i++) {
    let text = Paragraph[i].innerText;
    let words = text.split(" ");
    let count = words.length;
    console.log("paragraph" + (i + 1) + "has" + count + "words");
}

// ✅ Homework 3: Image Gallery Resize
// Select all <img> elements.
// Set their width to 200px and border radius to 10px.
// If the image alt text contains the word "cat", set the border color to orange.

let images = document.getElementsByName("img");
    for (let i =0; i <images.length; i++) {
        let img = images[i];
        img.style.width = "200px"
        img.style.borderRadius = "10px";
        img.style.border = "2px solid transparent";

        if (img.lastChild.toLowerCse().inCludes("cat")) {
            img.style.borderColor = "orange";
        }
    }



// ✅ Homework 4: Animate Circles
// Create 3 <div>s with the class "circle" using JavaScript.
// Style them as small circles (e.g., width and height 50px, border-radius: 50%, background: purple).
// Animate them moving right 10px every 200ms using setInterval.

for (let i = 0; i < 3; i++) {
    let circle = document.createElement("div");
    circle.className = "circle";
    circle.style.width = "50px";
    circle.style.height = "50px";
    circle.style.borderRadius = "50%";
    circle.style.background = "purple";
    circle.style.position = "absolute";
    circle.style.top = (i * 60) + "px";
    circle.style.left = "0px";
    document.body.appendChild(circle);

    let pos = 0;
    setInterval(() => {
        pos += 10;
        circle.style.left = pos + "px";
    }, 200);
}


// ✅ Homework 5: List Alternating Color
// Select all <li> tags.
// Give even-indexed items a background color of skyblue.
// Give odd-indexed items a background color of lightgray.

let itmes = document.getElementsByTagName("li");
for (let i = 0; i < itmes.length; i++) {
    if (i % 2 === 0) {
        items[i].style.backgroundColor = "skyblue";
    } else {
        items[i].style.backgroundColor = "lightgray";
    }
}


// ✅ Homework 6: Interactive Box Movement
// Create one <div> and one <button> with JavaScript.
// When the button is clicked:
// The box moves right by 20px.
// The background color randomly changes.

let div = document.getElementById ("div-main");
let button = document.getElementById("button-main");

let divleft = 0;

button.addEventListener("click", function(){
    divleft += 20;
    div.style.left = String(divleft) + "px";
})