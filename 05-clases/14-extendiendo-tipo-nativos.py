class List(list):
    def prepend(self, item):
        self.insert(0, item)

listNumbers = List([1, 2, 3])
listNumbers.append(4)

print(listNumbers)  # Output: [1, 2, 3, 4]

listNumbers.prepend(0)
print(listNumbers)  # Output: [0, 1, 2, 3, 4]