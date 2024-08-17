marks = float(input("Enter your mark: "))
if marks > 100:
    print("Enter valid mark")
elif marks >= 70:
    print("You passed with 'A'")
elif marks >= 60:
    print("You passed with 'B'")
elif marks >= 50:
    print("You passed with 'c'")
else:
    print("fail")
