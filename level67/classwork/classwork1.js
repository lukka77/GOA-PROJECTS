let keys = {
    name: "luka",
    surname: "gorgadze",
    academy: "GOA",
    city: "Batumi",
    role: "pupil",
    favColor: "White",

  logFullName() {
    console.log(this.name + " " + this.surname);
  },

  logFavColor() {
    console.log(this.favColor);
  }
};

console.log(keys);

console.log(keys.academy);

keys.logFavColor();
keys.logFavColor();

keys.city = "Tbilisi";
console.log(keys.city);