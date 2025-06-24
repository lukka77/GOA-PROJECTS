function addNewElement() {
    let div = document.getElementById("div1");

    let button = document.createElement("button");
    let buttonText = document.createTextNode("click");
    button.appendChild(buttonText);

    div.appendChild(button);
}

addNewElement()