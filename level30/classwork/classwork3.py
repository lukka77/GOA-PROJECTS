# საკლასო დავალება:
# მომხმარებელს შემოატანინეთ მთავარი სთრინგი და შეინახეთ main_str ცვლადში.
# შემდეგ შემოატანინეთ დასათვლელი სთრინგი და შეინახეთ str_to_count ცვლადში.
# დაბეჭდეთ str_to_count რამდენჯერ შეგხვდება main_str ცვლადში


main_str = input("მთავარი სტრიქონი: ")
str_to_count = input("დასათვლელი სტრიქონი: ")

count = main_str.count(str_to_count)
print(count)