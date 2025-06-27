def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        result = None
    except Exception as e:
        print(f"Another error: {e}")
        result = None
    finally:
        return result

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input, please enter valid value")
    num1 = None
    num2 = None
except Exception as e:
    print(f"Another error: {e}")
else:
    print("Result:", divide(num1, num2))
finally:
    print("Execution completed")
