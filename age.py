age = int(input("Enter your age: "))
if age < 5:
    price = "Free"
elif 5 <= age <= 18:
    price = "₹100"
elif 19 <= age <= 60:
    price = "₹200"
else:  
    price = "₹150"
print(f"Ticket Price: {price}")
