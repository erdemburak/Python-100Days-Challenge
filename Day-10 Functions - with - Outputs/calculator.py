def add(n1,n2):
    print(f"{n1} + {n2} = {n1+n2}")
    return n1 + n2

def subtract(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")
    return n1 - n2

def multiply(n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")
    return n1 * n2

def devide(n1, n2):
    print(f"{n1} / {n2} = {n1/n2}")
    return n1 / n2

def calculate(n1,n2,opt):
    if opt == "+":
        return add(n1,n2)
    elif opt == "-":
        return subtract(n1,n2)
    elif opt == "*":
        return multiply(n1,n2)
    elif opt == "/":
        return devide(n1,n2)


close_calculator = "n"

while close_calculator == "n":

    first_number = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_number = float(input("What's the next number?: "))

    calculator_result = calculate(first_number,second_number,operation)
          
    new_calculation = "n"
    new_calculation = input(f"Type 'y' to continue calculating with {calculator_result}, type 'n' to start a new calculator and type 'x' to exit: ").lower()
    if new_calculation == "x":
        close_calculator = "x"

    while new_calculation == "y":
        next_operation = input("+\n-\n*\n/\nPick an operation: ")
        next_number = float(input("What's the next number?: "))

        next_result = calculate(calculator_result, next_number, next_operation)
        new_calculation = input(f"Type 'y' to continue calculating with {next_result}, type 'n' to start a new calculator and type 'x' to exit: ").lower()
        if new_calculation == "x":
            close_calculator = "x"
