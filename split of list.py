# program 4 : Write a Python program to split a given list into two parts where the length of the first part of the list is given. 

my_list=[1, 1, 2, 3, 4, 4, 5, 1]
length=3
first_half=my_list[:length]
second_half=my_list[length:]
print("the first part and the second part of the original list is ",(first_half,second_half))

