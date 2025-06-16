def sum(*args):
    result = 0
    for arg in args:
        result += arg
    print(f"La suma de los argumentos es: {result}")

sum(1, 2, 3)
sum(4, 5, 6, 7, 8)
sum(10, 20, 30, 40, 50, 60, 70)
sum(100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)