class Calculator:

    def __init__(self):

        self.result = 0

    def add(self, num1, num2):

        return num1 + num2

    def subtract(self, num1, num2):

        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    
    def power(self, base, exponent):
        return base ** exponent
    
    def square_root(self, num):
        return num ** 0.5
    
    def factorial(self, num):
        if num < 0:
            raise ValueError("Cannot compute factorial of a negative number")
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result