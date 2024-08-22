str1 = 'Dilbert'
str2 = 'Dogbert'

str3 = str1 + str2 + 'Wally'
print(str3)

# Slicing from index 2 to 10
print(str3[2:10])

# Slicing from index 2 to 10 with step 2
print(str3[2:10:2])

# Slicing from index 10 to end
print(str3[14:])

# Slicing from 5 before the end to end
print(str3[-5:])

# String length
print(len(str3))

# String repetition
print(str1 * 3)

# String membership
print('Dil' in str1)

# Find the index of a substring
print(str3.find('Wally'))

# Find the index of a substring starting from a given index
print(str3.find('Wally', 10))

# Find returns -1 if the substring is not found
print(str3.find('Alice'))

# Count the number of occurrences of a substring
print(str3.count('b'))

# Replace a substring
print(str3.replace('Wally', 'Alice'))