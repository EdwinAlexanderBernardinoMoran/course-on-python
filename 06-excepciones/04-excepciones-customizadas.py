class MyError(Exception):
    "This is a custom exception."

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"{self.message}  - code: {self.code}"


def division(number = 0):
    if number == 0:
        raise MyError("Division by zero is not allowed.", 400)
    return 10 / number

try:
    division()
except MyError as e:
    print(e)