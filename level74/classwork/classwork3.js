// ეს ელემენტი წამოიღეთ js-ში და მასზე დაამატეთ მოვლენის მსმენელი. 
// მოვლენა უნდა იყოს pointerover, ხოლო ფუნქციას გაუწერეთ e პარამეტრი.
// ამ პარამეტრით მიწვდით target და დაბეჭდეთ ელემენტის ყველა ატრიბუტის მნიშვნელობა, ბოლოს დაბეჭდეთ თვითონ target.

let Link = document.getElementById("Link")

Link.addEventListener("pointerover", function(e) {
    let target = e.target;

    console.log("target: ", target)
})
