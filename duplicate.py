#program 3 : Write a Python program to find duplicate values from a list and display those. 

my_list=[1,2,2,3,3,4,5,5,6,7,7]
duplicates=[]
for list in my_list:
    if my_list.count(list)>1 and list not in duplicates:
        duplicates.append(list)
print("the duplicate items in list are",duplicates)
