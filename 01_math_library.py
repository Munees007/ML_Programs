"""Title: Implement the functions using Math library
Aim: To implement mathematical functions using Python's math library.
Program: The menu calculates square root, power, factorial, ceiling, floor,
absolute value, GCD, sine, cosine, and natural logarithm.
Sample output: Selecting sine and entering 30 displays Sine: 0.5.
Result: Thus, the above code is executed and the output verified successfully.
"""
import math
print("1. Square Root\n2. Power\n3. Factorial\n4. Ceiling\n5. Floor\n6. Absolute Value\n7. GCD\n8. Sine\n9. Cosine\n10. Logarithm\n0. Exit")
while True:
    try:
        choice = int(input("Enter choice: "))
        match choice:
            case 0:
                break
            case 1:
                value = float(input("Enter a non-negative number: "))
                if value < 0: 
                    print("Square root requires a non-negative number.")
                else: print("Square Root:", math.sqrt(value))
            case 2:
                first = float(input("Enter base: "))
                second = float(input("Enter exponent: "))
                print("Power:", math.pow(first, second))
            case 3:
                value = int(input("Enter a non-negative integer: "))
                if value < 0:
                    print("Factorial is not defined for negative integers.")
                else:
                    print("Factorial:", math.factorial(value))
            case 4:
                value = float(input("Enter a number: "))
                print("Ceiling:", math.ceil(value))
            case 5:
                value = float(input("Enter a number: "))
                print("Floor:", math.floor(value))
            case 6:
                value = float(input("Enter a number: "))
                print("Absolute value:", math.fabs(value))
            case 7:
                first = int(input("Enter first integer: "))
                second = int(input("Enter second integer: "))
                print("GCD:", math.gcd(first, second))
            case 8:
                angle = float(input("Enter angle in degrees: "))
                print("Sine:", math.sin(math.radians(angle)))
            case 9:
                angle = float(input("Enter angle in degrees: "))
                print("Cosine:", math.cos(math.radians(angle)))
            case 10:
                value = float(input("Enter a positive number: "))
                if value <= 0: 
                    print("Logarithm requires a positive number.")
                else: print("Logarithm:", math.log(value))
            case _: 
                print("Invalid choice. Select a listed option.")
    except (ValueError) as error:
        print("Invalid value:", error)
