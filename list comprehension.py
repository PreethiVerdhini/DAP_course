#program 4 : Write a Python program to create a list of squares of all even numbers from 1 to 20 using list comprehension,
#and then calculate the sum of all those squares.
squares = [x**2 for x in range(1, 21) if x % 2 == 0]
total = sum(squares)
print("Squares of even numbers from 1 to 20:", squares)
print("Sum of squares:", total)
