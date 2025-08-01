function cw(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10){
    for (let item of arguments){
        if (item %2 == 0){
            console.log(item)
        }
    }
}

cw(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)