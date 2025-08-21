// საკლასო დავალება:
// Prompt the user for two values. Use isNaN() to test each one and display whether they are numbers or not. log "Is number" if result is false, else log "Is not a number

const numberChekc = () => {
    const helperFunc = i => {
        if (isNaN(i)) {
            console.log("Is not a number")
        } else {
            console.log("Is number")
        }
    }

    const value1 = prompt("Enter value: ");
    const value2 =prompt("Enter value: ");

    helperFunc(value1);
    helperFunc(value2);
}

numberChekc()