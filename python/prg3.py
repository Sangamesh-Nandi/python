def reverse_array(arr):
    return arr[::-1]

input_string = input("Enter numbers separated by commas: ")
array = list(map(int, input_string.split(',')))
reversed_array = reverse_array(array)
print("Reversed array:", reversed_array)
