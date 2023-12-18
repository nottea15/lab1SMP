import math

memory = None
history = []
settings = {
    "decimal_places": 2,
    "use_memory": True
}


def show_history():
    global history
    print("History:")
    for item in history:
        print(item)


def save(value):
    global memory
    memory = value


def get_operator():
    while True:
        value = input("Enter operator (+, -, *, /, ^, √, %): ")
        if value not in ('+', '-', '*', '/', '^', '%', '√'):
            print(f"operator {value} is not valid")
        else:
            return value


def get_number(message):
    global memory
    global settings
    if memory is not None and settings["use_memory"] :
        print(f"Value in memory {memory}")
        use_from_memory = input("Do you want to use value from memory? (yes/no)")
        if use_from_memory.lower() == 'yes':
            return memory
    while True:
        try:
            return float(input(message))
        except:
            print("Incorrect number! Enter valid")


def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: you can't divide by zero")
            return None
        else:
            return num1 / num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '√':
        return math.sqrt(num1)
    elif operator == '%':
        return num1 % num2


def change_settings():
    global settings
    print("1. Change decimal places.")
    print("2. Toggle memory function.")

    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            places = int(input("Enter number of decimal places (0-10): "))
            if 0 <= places <= 10:
                settings["decimal_places"] = places
                print(f"Set decimal places to {places}.")
            else:
                print("Invalid number of decimal places.")
        except ValueError:
            print("Invalid input.")
    elif choice == '2':
        settings["use_memory"] = not settings["use_memory"]
        status = "enabled" if settings["use_memory"] else "disabled"
        print(f"Memory function is now {status}.")


def get_choice():
    while True:
        print("\nCalculator Menu:")
        print("1. Continue.")
        print("2. View history.")
        print("3. Change settings.")
        print("4. Quit.")

        choice = input("Enter your choice: ")
        if choice == "1":
            break
        elif choice == "2":
            show_history()
            continue_choice = input("Do you want to continue? (yes/no)")
            if continue_choice.lower() != 'yes':
                return 'close'
        elif choice == "3":
            change_settings()
            continue_choice = input("Do you want to continue? (yes/no)")
            if continue_choice.lower() != 'yes':
                return 'close'
        elif choice == "4":
            return 'close'
        else:
            print("Enter valid option")


while True:
    first_num = get_number("Enter first number: ")
    operation = get_operator()
    second_num = get_number("Enter second number: ")

    result = calculate(first_num, operation, second_num)
    if result is None:
        continue
    print(settings['decimal_places'])
    result = round(result, settings["decimal_places"])
    print(f"Result: {result}")

    history.append(f"{first_num} {operation} {second_num} = {result}")

    if settings["use_memory"]:
        save_choice = input("Do you want to save result? (yes, no)")
        if save_choice == 'yes':
            save(result)
            print(f"Value {result} is saved")
    else:
        memory = None

    option = get_choice()
    if option == "close":
        break