list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)

numbers = [10, 20, 30, 40, 50]

numbers.pop(2)          # Removes value at index 2 (30)
numbers.insert(2, 35)   # Add first new value
numbers.insert(3, 45)   # Add second new value

print(numbers)



fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

fruits.pop(0)   # Remove first element
fruits.pop()    # Remove last element

print(fruits)
