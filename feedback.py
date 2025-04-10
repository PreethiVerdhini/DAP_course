# program 4 : Take a feedback string and count how many times the word “good” appears in it (case-insensitive).

feedback1 = input("Enter feedback 1: ")
feedback2 = input("Enter feedback 2: ")
feedback3 = input("Enter feedback 3: ")
all_feedback = feedback1 + " " + feedback2 + " " + feedback3 
words = all_feedback.lower().split()
count = words.count("good")
print(f'\nThe word "good" appears {count} time(s).')
