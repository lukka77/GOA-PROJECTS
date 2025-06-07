function getFormData(e) {
    e.preventDefault();

    let form = document.getElementById("main-form0")
    let name = form.nextElementSibling.name.value;
    console.log(name)

    form.reset();
}