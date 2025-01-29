# შექმენით ფუნქცია სახელად remove_one_element, რომელსაც გადაეცემა სია და ინდექსი.
# სიიდან მაგ ინდექსზე მყოფი ელემენტი ამოშალეთ და დაბეჭდეთ სია.

def remove_one_element(list, ind):
    list.pop(ind)
    print(list)

list = [1, 2, 3, 4, 5]
remove_one_element(list, 2)