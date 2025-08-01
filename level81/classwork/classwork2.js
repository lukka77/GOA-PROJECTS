let ul = document.getElementById("ul-main")

let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
}

for (let key in myObj) {
    let li1 = document.createElement("li");
    li1.textContent = key;

    let li2 = document.createElement("li");
    liw.textContent = myObj[ket];

    let hr = document.createElement("hr");

    ul.appendChild(li1)
    ul.appendChild(li2)
    ul.appendChild(hr)
}