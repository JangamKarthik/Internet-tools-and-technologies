
def is_palindrome(string):
    clean_string = ''.join(char.lower() for char in string if char.isalnum())
    return clean_string == clean_string[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
