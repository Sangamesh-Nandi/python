#Python program to add two binary numbers
def add_binary(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

bin1 = input("Enter the first binary number: ")
bin2 = input("Enter the second binary number: ")

print(f"The sum of {bin1} and {bin2} is {add_binary(bin1, bin2)}")
