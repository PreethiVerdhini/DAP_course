 # program 4 : .Create a contact book using a dictionary where the name is the key and phone number is the value.
 #Allow the user to input a name and phone number. If the name exists, update the number; otherwise, insert a new contact.


contacts = {
    "pree": "8867239590",
    "jay": "7406302545"
}
name = input("Enter contact name: ")
phone = input("Enter phone number: ")
if name in contacts:
    print(f"{name} already exists with number {contacts[name]}. Updating number...")
else:
    print(f"Adding new contact: {name}")
contacts[name] = phone
print("\nUpdated Contact Book:")
for contact_name, number in contacts.items():
    print(f"{contact_name}: {number}")
