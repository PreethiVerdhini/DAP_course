# program  5 : Write a Python program to traverse a given list in reverse order, and print the elements with the original index


my_list= ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
for i in range(len(my_list) - 1, -1, -1):
    print(f"Index: {i}, Value: {my_list[i]}")

