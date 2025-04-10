def sum_of_evens(start, end):
    even_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_sum += num
    return even_sum
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = sum_of_evens(start, end)
print(f"The sum of even numbers from {start} to {end} is: {result}")
