let div = document.getElementById("div1");
for (let i = 0; i < 5; i++){
    let p = document.createElement("p");
    let pText = document.createTextNode("Pargraph N" + String(pCount));
    p.appendChild(pText);

    pCount++;
    div.appendChild(p);
}