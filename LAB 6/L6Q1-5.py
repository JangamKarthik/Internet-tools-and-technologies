import re

def find_replace_string(input_string, pattern, replacement):
    return re.sub(pattern, replacement, input_string)

input_string = input("Enter a string: ")
pattern_to_replace = input("Enter the pattern to replace: ")
replacement_string = input("Enter the replacement string: ")

result_string = find_replace_string(input_string, pattern_to_replace, replacement_string)
print(f"String after replacement: {result_string}")
