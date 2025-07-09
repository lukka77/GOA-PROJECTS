// 1. Click Alert
document.getElementById("alertBtn").addEventListener("click", () => {
  alert("Button was clicked!");
});

// 2. Change Text on Hover
let hoverPara = document.getElementById("hoverPara");
hoverPara.addEventListener("mouseenter", () => {
  hoverPara.textContent = "You hovered over me!";
});
hoverPara.addEventListener("mouseleave", () => {
  hoverPara.textContent = "Hover over me!";
});

// 3. Toggle Background Color
let toggleDiv = document.getElementById("toggleDiv");
let toggled = false;
toggleDiv.addEventListener("click", () => {
  if (toggled) {
    toggleDiv.style.backgroundColor = "lightgray";
  } else {
    toggleDiv.style.backgroundColor = "lightgreen";
  }
  toggled = !toggled;
});

// 4. Log Input Value on Click
document.getElementById("logInput").addEventListener("click", (e) => {
  console.log("Input value:", e.target.value);
});

// 5. Show/Hide Image on Button Click
let toggleImage = document.getElementById("toggleImage");
let toggleImgBtn = document.getElementById("toggleImgBtn");

toggleImgBtn.addEventListener("click", () => {
  if (toggleImage.style.display === "none") {
    toggleImage.style.display = "block";
  } else {
    toggleImage.style.display = "none";
  }
});