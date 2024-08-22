mylist = [1, 2, 3, 4, 5]

# Print the list
print(mylist)

# Print the first element
print(mylist[0])

# Print the last element
print(mylist[-1])

# Print the first 3 elements
print(mylist[0:3])

# Print the length of the list
print(len(mylist))

# Print the list twice
print(mylist * 2)

# Create a two-dimensional list
mylist2 = [[1, 2], [3, 4], [5, 6]]
print(mylist2[1][1])

# Add an element to the end of the list
mylist.append(6)
print(mylist)

# Add an element to the beginning of the list
mylist.insert(0, 0)
print(mylist)

# Remove the last element
mylist.pop()
print(mylist)

# Remove the first element
mylist.pop(0)
print(mylist)

# Remove the first element with the value 3
mylist.remove(3)
print(mylist)

# Sort the list
mylist.sort()
print(mylist)

# Reverse the list
mylist.reverse()
print(mylist)

# Clear the list
mylist.clear()
print(mylist)