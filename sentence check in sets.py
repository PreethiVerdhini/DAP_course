# program 4 : Check for Duplicate Words in a Sentence


sentence = "the sky is blue and the grass is green"
words = sentence.split()
unique_words = set(words)
if len(unique_words) < len(words): 
    print("The sentence has duplicate words.")
else:
    print("No duplicate words found.")
