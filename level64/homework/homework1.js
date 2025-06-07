function updateP() {
    let userInfo = prompt("Enter information:")

    let p = document.getElementById("p-main");

    p.textContent = userInfo;
}

updateP();