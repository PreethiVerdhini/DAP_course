# program 2 : Given a list of names,group them into a dictionarywhere the key is the first letter
#of each name and the value is a list of names that start with that letter.

names = ["Preethi", "Pranay", "Sailaja", "Suresh", "Divya", "Ram", "Virat", "Vijay"]
grouped_names = {}
for name in names:
    grouped_names.setdefault(name[0].upper(), []).append(name)
print("\nGrouped Names:", grouped_names)
