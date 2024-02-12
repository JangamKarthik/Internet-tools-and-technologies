import re

states = "Mississippi Alabama Texas Massachusetts Kansas"

statesList = []

while True:
    print("\nMenu:")
    print("1. Search for a word that ends in 'xas'")
    print("2. Search for a word that begins with 'k' and ends in 's'")
    print("3. Search for a word that begins with 'M' and ends in 's'")
    print("4. Search for a word that ends in 'a'")
    print("5. Search for a word that begins with 'M' at the beginning of the string")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        match_xas = re.search(r'\bxas\b', states)
        if match_xas:
            statesList.append(match_xas.group())
    elif choice == '2':
        match_k_s = re.search(r'\b[kK].*s\b', states)
        if match_k_s:
            statesList.append(match_k_s.group())
    elif choice == '3':
        match_M_s = re.search(r'\b[Mm].*s\b', states)
        if match_M_s:
            statesList.append(match_M_s.group())
    elif choice == '4':
        match_a = re.search(r'\ba\b', states)
        if match_a:
            statesList.append(match_a.group())
    elif choice == '5':
        match_M_start = re.search(r'\b[Mm].*', states)
        if match_M_start:
            statesList.append(match_M_start.group())
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("States List:", statesList)
