result = int(input("Please enter your result: "))
if result >= 50:
    # it's 50 or above
    if result == 50:
        print("well done")
    elif result > 90:
        print("excellent work")
    else:
        print("good score")
else:
    print("better luck next time")
    # It's less than 50
