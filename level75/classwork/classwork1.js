  let id = setInterval(function() {
    console.log("Luka Gorgadze");
  }, 10000);

  function stopInterval() {
    clearInterval(id);
    console.log("Stop!");
  }