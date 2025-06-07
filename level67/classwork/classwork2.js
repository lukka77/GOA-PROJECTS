function userOperations() {
    let answer1 = confirm("Do you like write codes?");
    let answer2 = confirm("Do you like play gmaes?");

    console.log("AND:", answer1 && answer2);
    console.log("OR:", answer1 || answer2);
}