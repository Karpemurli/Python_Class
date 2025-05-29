# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# Sample List
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Removing 0th, 4th, and 5th elements
filtered_colors = [colors[i] for i in range(len(colors)) if i not in [0, 4, 5]]

# Display the output
print(filtered_colors)
