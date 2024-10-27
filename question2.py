grades = input("Enter your grades: ")
grades1 = list(grades)
for i in grades1:
    if i >= 50:
        print("Pass")
    else:
        print("Fail")
