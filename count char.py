#program 2 :  Function to Count Occurrences of a Character in a String

def count_char_occurrences(s, char):
    return s.count(char)
string = "hello"
char_to_count = "l"
result = count_char_occurrences(string, char_to_count)
print(result)  
