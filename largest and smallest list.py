# program 2 :  Write a Python program to get the largest and smallest number from a list without builtin functions

my_list=[1,2,3,4,5,6]
largest=my_list[0]
smallest=my_list[0]
for list in my_list:
    if list>largest:
        largest=list
    if list<smallest:
        smallest=list
print("the largest number is:",largest)
print("the smallest number is:",smallest)
