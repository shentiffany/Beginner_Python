def calculate_factorial(number):
    if type(number) == int:
        print("The factorial of " + str(number) + " is", end =" ")
        if number > 0:
            for i in reversed(range(number)):
                if i > 0:
                    number = number * i
        elif number == 0:
            number = 1
        else:
            print("Undefined.")
        print(number)
    else:
        print("Please input an integer.")
calculate_factorial(5)