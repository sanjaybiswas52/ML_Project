import copy

# Create a nested list
original_list = [1, 2, [3, 4]]

# Shallow copy - only the outer list is copied
shallow_copy = copy.copy(original_list)

# Deep copy - once copy 
deep_copy = copy.deepcopy(original_list)

# Modify the nested list
original_list[2][0] = 99

# Results
print("Original List:", original_list)  # Original List: [1, 2, [99, 4]]
print("Shallow Copy:", shallow_copy)    # Shallow Copy: [1, 2, [99, 4]]
print("Deep Copy:", deep_copy)          # Deep Copy: [1, 2, [3, 4]]