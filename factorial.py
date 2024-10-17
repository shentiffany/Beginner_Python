def calculate_factorial(number):
    if type(number) == int:
        print("The factorial of " + str(number) + " is", end =" ")
        if number > 0:
            for i in reversed(range(number)):
                if i > 0:
                    number = number * i
                    print(number)
        elif number == 0:
            number = 1
            print(number)
        else:
            print("Undefined.")
    else:
        print("Please input an integer.")
calculate_factorial() # try this
