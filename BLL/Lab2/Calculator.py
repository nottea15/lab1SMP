import math


class Calculator:
    def __init__(self):
        self.history = []
        self.memory = None
        self.settings = {"decimal_places": 2, "use_memory": True}

    def get_number(self, message: str) -> float:
        if self.memory is not None and self.settings["use_memory"]:
            print(f"Value in memory {self.memory}")
            use_from_memory = input("Do you want to use value from memory? (yes/no)")
            if use_from_memory.lower() == 'yes':
                return self.memory
        while True:
            try:
                return float(input(message))
            except:
                print("Incorrect number! Enter valid")

    def get_operator(self) -> str:
        while True:
            value = input("Enter operator (+, -, *, /, ^, √, %): ")
            if value not in ('+', '-', '*', '/', '^', '√', '%'):
                print(f"Operator {value} is not valid")
            else:
                return value

    def calculate(self, num1: float, operator: str, num2: float) -> float:
        operations = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2,
                      '^': num1 ** num2}
        if operator == '/':
            if num2 == 0:
                print("Error: you can't divide by zero")
                return None
            else:
                return num1 / num2
        elif operator == '%':
            if num2 == 0:
                print("Error: you can't modulo by zero")
                return None
            else:
                return num1 % num2
        elif operator == '√':
            if num1 < 0:
                print("Error: you can't get root of negative")
                return None
            else:
                return math.sqrt(num1)
        else:
            return operations[operator]

    def save(self, value: float) -> None:
        self.memory = value

    def start_calculator(self) -> None:
        while True:
            first_num = self.get_number("Enter first number: ")
            operation = self.get_operator()
            second_num = self.get_number("Enter second number: ")

            result = self.calculate(first_num, operation, second_num)
            if result is None:
                continue
            result = round(result, self.settings["decimal_places"])
            print(f"Result: {result}")

            self.history.append(f"{first_num} {operation} {second_num} = {result}")

            if self.settings["use_memory"]:
                save_choice = input("Do you want to save result? (yes, no)")
                if save_choice == 'yes':
                    self.save(result)
                    print(f"Value {result} is saved")
            else:
                self.memory = None

            self.call_menu()

    def call_menu(self) -> None:
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
                self.show_history()
                continue_choice = input("Do you want to continue? (yes/no)")
                if continue_choice.lower() != 'yes':
                    return
            elif choice == "3":
                self.change_settings()
                continue_choice = input("Do you want to continue? (yes/no)")
                if continue_choice.lower() != 'yes':
                    return
            elif choice == "4":
                return
            else:
                print("Enter valid option")

    def change_settings(self) -> None:
        print("1. Change decimal places.")
        print("2. Toggle memory function.")

        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                places = int(input("Enter number of decimal places (0-10): "))
                if 0 <= places <= 10:
                    self.settings["decimal_places"] = places
                    print(f"Set decimal places to {places}.")
                else:
                    print("Invalid number of decimal places.")
            except ValueError:
                print("Invalid input.")
        elif choice == '2':
            self.settings["use_memory"] = not self.settings["use_memory"]
            status = "enabled" if self.settings["use_memory"] else "disabled"
            print(f"Memory function is now {status}.")

    def show_history(self) -> None:
        print("History:")
        for item in self.history:
            print(item)

