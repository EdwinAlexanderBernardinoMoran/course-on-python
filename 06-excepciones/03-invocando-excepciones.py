def division(number = 0):
    if number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return 10 / number

try:
    division()
except ZeroDivisionError as e:
    print(e)