#program 3 : Write a Python program to find the sum of digits of a number using a while loop
n = int(input("Enter a number: "))
s = 0

while n > 0:
    s += n % 10
    n //= 10

print("Sum of digits:", s)
