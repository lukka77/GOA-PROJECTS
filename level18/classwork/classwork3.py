# საკლასო დავალება 3: 
# 10-დან 30-ის ჩათვლით დაბეჭდეთ ყველა რიცხვი და თან მიუწერეთ ლუწია თუ კენტი,
# მაგ: 10 - even, 11 - odd, 12 - even და ასე გაგრძელდება 30-ის ჩათვლით

# even - ლუწი
# odd - კენტი

for num1 in range(10, 31):
     if num1 %2 == 0:
       print(str(num1), "- even")
     else:
       print(str(num1), "- odd")