# Move the content of targets.txt into two separate files

# Open the file for reading and read it into a list
with open('targets.txt', 'r') as f:
    lines = f.readlines()

print('List:')
print(lines)

# Organize the data into a dictionary
d = {}
for line in lines:
    parts = line.split() # Split the line into two parts based on whitespace
    d[parts[0]] = parts[1]

print('Dictionary:')
print(d)

# Write the dictionary to two separate files
for key, value in d.items():
    targets = value.split(',')
    filename = key + '.targets'
    with open(key + '.tgt', 'w') as f:
        for target in targets:
            f.write(target + '\n')
