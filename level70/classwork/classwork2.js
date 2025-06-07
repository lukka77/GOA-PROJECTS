// საკლასო დავალება:

// html-ის დოკუმენტში დაამატეთ ერთი ინფუთი, ერთი ღილაკი და ერთი სათაური.

// external js-ში შექმენით ფუნქცია სახელად changeElements. 

// ამ ფუნქციაში წამოიღეთ ელემენტები id-ის გამოყენებით.

// 1) დაადგინეთ input-ის value და გამოიტანეთ კონსოლში.
// 2. ღილაკის ფონის ფერი გახადეთ შავი, ხოლო ტექსტის ფერი თეთრი.
// 3) სათაურის textAlign-ის მნიშვნელობა გაწერეთ center.
// 4) მთლიანი დოკუმენტის ფონის ფერი დააყენეთ მწვანე


function changeElements() {
    let input = document.getElementById("myInput");
    let button = document.getElementById("myButton");
    let title = document.getElementById("myTitle");

    console.log(input.vlaue);
    button.style.background = "black";
    button.style.color= "white";
    title.style.textAlign = "center";
    document.body.style.background = "blue";
}