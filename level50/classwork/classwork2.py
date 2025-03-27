# 2)მომხმარებელს შემოატანინეთ რაღაც მონაცემი (მაგ:სახელი ან გვარი) და try,except ბლოკების საშუალებით გააკონტროლეთ 
# ყველა ერორის შემთხვევა რაც არსებობს

name = input("Enter your name: ")

try:
    print(len(name))
except TypeError:
    print("TypeError!")
except IndexError:
    print("IndexError!")
except NameError:
    print("NameError!")
except SyntaxError:
    print("SyntaxError!")