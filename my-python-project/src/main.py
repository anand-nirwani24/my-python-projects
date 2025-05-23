from calculator import Calculator

def main():
    print("Welcome to the Python Calculator!")
    calc = Calculator()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Addition: {calc.add(num1, num2)}")
        print(f"Subtraction: {calc.subtract(num1, num2)}")
        print(f"Multiplication: {calc.multiply(num1, num2)}")
        try:
            print(f"Division: {calc.divide(num1, num2)}")
        except ValueError as e:
            print(f"Division: {e}")
        print(f"Power (num1^num2): {calc.power(num1, num2)}")
        print(f"Square root of first number: {calc.square_root(num1)}")
        print(f"Square root of second number: {calc.square_root(num2)}")
        # print(f"factorial of num1: {calc.factorial(num1)}")
        # print(f"factorial of num2: {calc.factorial(num2)}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()