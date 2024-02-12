import string

def remove_punctuations(input_string):
    return input_string.translate(str.maketrans("", "", string.punctuation))

input_string = input("Enter a string: ")

result_string = remove_punctuations(input_string)
print(f"String after removing punctuations: {result_string}")
