def task_one():
    kilos = float(input("Enter a value in kilograms: "))


    pounds = float(input("Enter a value in pounds: "))


    converted_pounds = kilos * 2.20462


    converted_kilos = pounds * 0.453592


    print(f"kilograms to punds: {converted_pounds}")
    print(f"Pounds to Kilograms: {converted_kilos}")

def task_two():
        
    number = int(input("Enter a three-digit number: "))

    
    if 100 <= number <= 999:
    
        hundreds = number // 100
        remainder = number % 100
        tens = remainder // 10
        units = remainder % 10

        print("Hundreds:", hundreds)
        print("Tens:", tens)
        print("Units:", units)
    else:
        print("Please enter a valid three-digit number.")

def task_three():
    a = "Password length verification ensures security by requiring longer, harder-to-crack passwords."

    password = "Nat3ha123"
    minLength = 8  
    if len(password) >= minLength:
        return True 
    else:
        return False

def task_four():
    print("Variables for changing values, constants for values that should never change, like mathematical constants (e.g., pi)")

def task_five():
    print("Auto-Completion: Helps complete code and reduce errors.\nSyntax Highlighting: Highlights code with colors to identify syntax elements for clarity.")
    print("Code Debugging Tools: Allow setting breakpoints and step through code.\nError Messages: Provides detailed error messages to pinpoint issues.\nCode Analysis: Identifies potential logic errors through static analysis or linting.")

