set1 = set(map(int, input("Enter elements of the first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of the second set separated by spaces: ").split()))

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2

print(f"Union: {union_set}, Intersection: {intersection_set}, Difference: {difference_set}")
