# program 3 : You have a dictionary. Ask the user to enter a key and display the corresponding value. Handle the KeyError.

data = {
    "name": "Pree",
    "age": 21,
    "city": "Bangalore",
    "profession": "Student"
}

try:
   key = input("Enter a key (name, age, city, profession): ")
   print(f"The value for '{key}' is: {data[key]}")
except KeyError:
    print("Error: The key entered does not exist in the dictionary.")


