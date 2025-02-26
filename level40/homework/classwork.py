#  თავიდან შეასრულეთ საკლასო დავალებები. კომენტარების სახით ახსენით თითოეული ფუნქცია:

# 1) Function 1 - hello world
def greet():
    return "hello world!"
# აბრუნებს ტექსტს "hello world!".


# 2) Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)
# დავითვალოთ რამდენი სიმბოლო True არსებობს სიაში.


# 3) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")
# ამოიღოს ყველა ცარიელი ადგილი მოცემულ სტრიქონიდან.

# 4) You Can't Code Under Pressure #1
def double_integer(i):
    return i*2
# გადაცემული i-ის რაოდენობა გაორმაგდება.


# 5) Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"
# მომხმარებლის სახელით ხდება მისალმება.


# 6) Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)
# ბულეანის მნიშვნელობის (True ან False) გადატანა სტრიქონად.


# 7) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
# გვაქვს 2 რიცხვი(vlaue1, value2) რომლებიც, შეგვიძლია შევკრიბოთ გამოვაკლოთ გავამრავლოთ და გავყოთ ერთმანეთზე.


# 8) Keep Hydrated!
def litres(time):
    return time // 2
# დროის გამოყენების მიხედვით, რამდენი ლიტრი წყალი უნდა დალიოთ.


# 9) Century From Year
def century(year): 
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
# რომელ საუკუნეში შედის მოცემული წელი.
    

# 10) Convert number to reversed array of digits
def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]

    res_list = []

    for i in reversed_str:
        res_list.append(int(i))

    return res_list
# ვიღებთ რიცხვს და ვაკონვერტირებთ მის ციფრებს სიად, სადაც თითოეული ციფრი იქნება ცალკე ელემენტი.


# 11) Beginner - Lost Without a Map
def maps(a):
    saver=[]
    for i in a:
        saver.append(i*2)
    return saver
# ჩვენ ვზრდით ყველა ელემენტს სიაში, მაგრამ თითოეული ელემენტი გაორმაგებულია.

# 12) Opposites Attract
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2)%2 == 1
# განსაზღვრა ხდება იმისა რომ, ორივე flower-ის რაოდენობის შეეხამება.

# 13) Sum Arrays
def sum_array(a):
    return sum(a)
# ვაბრუნებთ რიცხვების ჯამს.



# 2) შეასრულეთ შემდეგი 5 ამოცანა:

# 1
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

# 2
def make_upper_case(s):
    return s.upper()

# 3) Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which returns the time since midnight in milliseconds.
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

# 4) Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# 5) Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F
def abbrev_name(name): 
    name = name.split() 
    return name[0][0].upper() + "." + name[1][0].upper()