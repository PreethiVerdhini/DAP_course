def find_largest(i):
    largest = i[0]  
    for num in i:
        if num > largest:
            largest = num
    return largest
numbers = [10, 20, 5, 8, 25, 3]
largest_number = find_largest(numbers)
print(f"Largest number is: {largest_number}")
