#program 3 : Write a program that removes extra spaces from a user-entered message.

message = input("Enter your message: ")
clean_message = ' '.join(message.split())
print("\nCleaned Message:")
print(clean_message)
