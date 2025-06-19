def large(text):
    result = 0
    for _ in text:
        result += 1
    return result

print("Debugging Functions Example")
l = large("Hello, world!")
print(l)