def find_max_index(arr):
    max_value = max(arr)  # Find the maximum value in the array
    max_index = arr.index(max_value)  # Find the index of the maximum value
    return max_index

# Example usage
my_array = [10, 5, 20, 8, 15]
max_index = find_max_index(my_array)
print("Index of max value:", max_index)