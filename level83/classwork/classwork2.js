// შემქენით arrow function სადაც პარამეტრად გადასცემტ სიას.სიაში იქნება 10 ცალი სტრინგი.გამოიტანეთ მხოლოდ ისეთი სტრინგები რომელთა სიგრძე მეტი იქნება ხუთზე

const wordss = ["apple", "banana", "car", "dog", "house", "GOA" ]

const longStrings = (strings) => {
    for(let i = 0; i < strings.length; i++){
        if(strings[i].length < 5) {
            continue;
        }
        console.log(strings[i])
    }
}

longStrings(wordss)