let div = document.getElementById("div1")
let h2 = document.getElementById("h2-main")

let numbersSum = 0;

do {
    let userNum = Number(promt("Enter number: "));
    numbersSum += userNum;

    let newP = document.createElement("p");
    let pText = document.createTextNode(userNum);
    newP.appendChild(pText);

    div.appendChild(newP);

    h2.textContet = numbersSum;
} while (numbersSum <= 100)