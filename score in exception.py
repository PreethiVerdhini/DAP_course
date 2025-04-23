# program 2 :  Create a program to validate exam scores entered by the user. Use a custom exception to handle invalid scores.


class InvalidScoreError(Exception):
    def __init__(self, message="Score must be between 0 and 100."):
        super().__init__(message)
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"Invalid score: {score}. Score must be between 0 and 100.")
    return f"Score {score} is valid!"
try:
   score = int(input("Enter the exam score: "))
   print(validate_score(score))
except InvalidScoreError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid integer for the score.")

