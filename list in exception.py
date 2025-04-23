#program 1 : .Write a program that asks the user for a list index and prints the value at that index from a predefined list.
#Handle the IndexError and ValueError exceptions

my_list = ['Laptop', 'Desktop', 'Tablet', 'Ipad']

try:
    index = int(input("Enter the index of the item you want (0-3): "))
    print(f"The item at index {index} is {my_list[index]}")
except IndexError:
    print("Error: The index you entered is out of range. Please enter a value between 0 and 3.")
except ValueError:
    print("Error: Please enter a valid integer.")

