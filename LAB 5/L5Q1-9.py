def is_palindrome(lst):
    return lst == lst[::-1]

input_list = list(input("Enter a list of elements separated by spaces: ").split())

if is_palindrome(input_list):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
