const myArr = ["Luka", "Gorgadze", 10, 20, true, false]
for (let item of myArr){
    if(typeof item === "string"){
        console.log(item)
    } else if (typeof item === "number"){
        console.log(item + 10);
    } else if (typeof item === "boolean"){
        console.log(item)
    }
}