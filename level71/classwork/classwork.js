function startGame() {
    const randomNumber = Math.floor(Math.random() * 100) + 1;
    let guess;

    while (true) {
    guess = prompt("შეიყვანეთ რიცხვი 1-დან 100-მდე:");

    if (guess === null) {
        alert("თამაში შეწყდა.");
        break;
    }

    guess = Number(guess);

    if (isNaN(guess) || guess < 1 || guess > 100) {
        alert("გთხოვთ, შეიყვანოთ სწორი რიცხვი 1-დან 100-მდე!");
        continue;
    }

    if (guess > randomNumber) {
        alert("მეტია");
    } else if (guess < randomNumber) {
        alert("ნაკლებია");
    } else {
        alert("გილოცავ! სწორად გამოიცანი 🎉");
        break;
    }
    }
}