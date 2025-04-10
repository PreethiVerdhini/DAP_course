def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"Even numbers count: {even_count}")
    print(f"Odd numbers count: {odd_count}")
input_list = input("Enter a list of integers separated by spaces: ")
numbers = list(map(int, input_list.split()))
count_even_odd(numbers)
