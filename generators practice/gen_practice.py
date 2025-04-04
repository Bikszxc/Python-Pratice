while True:
    try:
        user_input = int(input("Enter a number: "))
        print("Yehey!")
        break
    except ValueError:
        print("Not a number!")