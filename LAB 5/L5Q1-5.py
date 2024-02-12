def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)

num = int(input("Enter a natural number: "))

print(f"Sum of natural numbers up to {num}: {sum_of_natural_numbers(num)}")
