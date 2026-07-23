is_logged_in = False
if is_logged_in:
    print("Welcome back!")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
