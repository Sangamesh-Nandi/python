from collections import Counter

def find_duplicates(s):
    return {char for char, count in Counter(s).items() if count > 1}

string = input("Enter a string: ")
duplicates = find_duplicates(string)

print("Duplicate characters:", ', '.join(duplicates) if duplicates else "No duplicate characters found.")
