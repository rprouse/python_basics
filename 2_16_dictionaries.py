d = { 'hero': 'Batman', 'villain': 'Joker' }
print(d['hero'])

# Add a new key-value pair
d['sidekick'] = 'Robin'
print(d)

# Remove a key-value pair
del d['villain']
print(d)

# Check if a key exists
print('hero' in d)

# Get the keys
print(d.keys())

# Get the values
print(d.values())

# Get the key-value pairs
print(d.items())

# Clear the dictionary
d.clear()
print(d)