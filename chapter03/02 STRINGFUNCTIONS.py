# String Variable
name = "  himanshi chouhan  "

# Convert all characters to lowercase
print(name.lower())

# Convert all characters to uppercase
print(name.upper())

# Capitalize only the first character
print(name.capitalize())

# Capitalize the first letter of each word
print(name.title())

# Remove spaces from both ends
print(name.strip())

# Remove spaces from the left side
print(name.lstrip())

# Remove spaces from the right side
print(name.rstrip())

# Replace one substring with another
print(name.replace("himanshi", "Himanshi"))

# Split string into a list of words
print(name.split())

# Join words using '-'
print("-".join(name.split()))

# Find the position of a substring
print(name.find("chouhan"))

# Find the position of a substring (gives error if not found)
print(name.index("chouhan"))

# Check if string starts with a space
print(name.startswith(" "))

# Check if string ends with a space
print(name.endswith(" "))

# Count occurrences of a character
print(name.count("h"))

# Check if string contains only alphabets
print(name.strip().isalpha())

# Check if string contains only digits
print("123".isdigit())

# Check if string contains only letters and numbers
print("himanshi123".isalnum())

# Check if string contains only whitespace
print("   ".isspace())

# String formatting using format()
print("My name is {}".format(name.strip()))

# Center the string within 30 characters
print(name.strip().center(30))

# Fill leading zeros until length becomes 5
print("42".zfill(5))

# f-string formatting
print(f"My name is {name.strip()}")

# Length of the string
print(len(name))

# Reverse the string
print(name[::-1])

# Check if a substring exists in the string
print("himanshi" in name)

# Get first character
print(name[0])

# Get last character
print(name[-1])

# Get a slice of the string
print(name[2:10])