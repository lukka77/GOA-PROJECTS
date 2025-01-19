#შექმენით ფუნქცია, სახელად manual_find, რომელსაც გაწერილი ექნება 2 პარამეტრი: main_string და str_to_find.

# ამ ფუნქციის დავალებაა რომ main_string-ში იპოვოს str_to_find მერამდენე ინდექსზეა.

# თუ მთავარ სთრინგში საძიებელი სთრინგი უბრალოდ არ გვაქვს, დავბეჭდოთ -1


def manual_find (main_string,str_to_find):
    result = -1

    for char in range(len(main_string)):
        if main_string[char] == str_to_find: result=char 

        if result == -1:
            print("String index not found")
        else:
            print(result)


manual_find("hello hello", "l")