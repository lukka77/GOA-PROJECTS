# საკლასო დავალება:
# შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

# თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def manual_list(start, end, step, user_num):
    return [num for num in range(start, end, step) if num > user_num]

print(manual_list(3, 12, 45, 2))
print(manual_list(15, 21, 7, 25))
print(manual_list(1, 41, 20, 9)) 
