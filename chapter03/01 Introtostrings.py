# STRING = are sequence of characters written inside quotes. It can include letters,
# numbers, symbols and spaces.Python does not have a separate character type
# and string is  imutable
a = "Himanshi"
b = 'himanshi'
c = '''himanshi'''

#STRING SLICING:
# Syntax=string[start:stop:step]
text = "Python"

print(text[0:4])     # 'Pyth'   (from index 0 to 3)
print(text[:4])      # 'Pyth'   (start omitted → 0)
print(text[2:])      # 'thon'   (stop omitted → till end)
print(text[::2])     # 'Pto'    (step = 2, skips characters)
print(text[::-1])    # 'nohtyP' (step = -1, reverses string)

# SLICING WITH SKIP VALUE
word = "amazing"
alternate = word[1:6:2]  # Output: "mzn"
# Explanation: Starts at index 1 ('m'), stops before index 6, skips 1 char (step=2)Copied!

