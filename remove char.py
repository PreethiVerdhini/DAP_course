#program 1 :  Function to Remove Specific Character from a String

def remove_char(s, char):
    return s.replace(char, '')
string = "hello"
char_to_remove = "l"
result = remove_char(string, char_to_remove)
print(result)  


