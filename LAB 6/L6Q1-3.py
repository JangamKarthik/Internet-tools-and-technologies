def sort_words_alphabetically(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)

input_string = input("Enter a string: ")

result_string = sort_words_alphabetically(input_string)
print(f"Words in alphabetic order: {result_string}")
