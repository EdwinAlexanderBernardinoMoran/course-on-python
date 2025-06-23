numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()  # Ordena la lista en su lugar
print(numbers)

numbers.sort(reverse=True)  # Ordena la lista en orden descendente
print(numbers)

newNumbers = [3, 7, 8, 2, 1, 4]
newNumbersSorted = sorted(newNumbers)  # Crea una nueva lista ordenada
print(newNumbersSorted)

users = [
    ["John", 30],
    ["Jane", 25],
    ["Alice", 28],
    ["Bob", 22]
]

def order(user):
    return user[1]  # Ordena por la edad (segundo elemento de cada sublista)

users.sort(key=order, reverse=True)  # Ordena por edad en orden descendente
print(users)