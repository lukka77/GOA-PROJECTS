# codewars


# 1) Get the mean of an array
def get_average(marks):
    return int(sum(marks) / len(marks))

# 2) Keep up the hoop
def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"

# 3) Reversed Words
def reverse_words(s):
    return " ".join(s.split(' ')[::-1])

# 4) Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int(s*27.777778)

# 5) Switch it Up!
def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]

# 6) Function 2 - squaring an argument
def square(n):
    return n*n

# 7) Removing Elements
def remove_every_other(my_list):
    new_list = []
    
    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])
    
    return new_list

# 8) Twice as old
def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)
    
    if res < 0: return res*-1
    return res

# 9) Is it even?
def is_even(n): 
    return n % 2 == 0

# 10) Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll*2

# 11) Get Planet Name By ID
def get_planet_name(id):
    if id == 1: return "Mercury"
    elif id == 2: return "Venus"
    elif id == 3: return "Earth"
    elif id == 4: return "Mars"
    elif id == 5: return "Jupiter"
    elif id == 6: return "Saturn"
    elif id == 7: return "Uranus"
    elif id == 8: return "Neptune"

# 12) Will there be enough space?
def enough(cap, on, wait):
    return max(0, wait - (cap - on))

# 13) Powers of 2
def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]


# 
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 24
    else:
        cat_years = 24 + (human_years - 2) * 4

    # For the dog:
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 24
    else:
        dog_years = 24 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]