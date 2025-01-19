#საკლასო დავალება:
# შექმენით ფუნქცია სახელად manual_swapcase

def manual_swapcase(main_str):
    res = " "
    for char in main_str:
        if char.islower(): res += char.upper()
    else:  res += char.lower()
    print(res)

print(manual_swapcase("Goa ACAdemY"))
print("Goa ACAdemY".swapcase())