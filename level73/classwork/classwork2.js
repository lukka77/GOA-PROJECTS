function replaceAndRemove(){
  let div = document.getElementById("div1");

  let button = document.getElementById("b");
  div.removeChild(button);

  let p = document.getElementById("p1");
  let i = document.createElement("i");
  let iText = document.createTextNode("hello");
  i.appendChild(iText)

  div.replaceChild(i, p)
  
}

replaceAndRemove()