function alertText(e){
    e.preventDefault();

    let input = document.getElementById("name-input");

    let val = input.value;
    alert(val)
    input.value = "";
}