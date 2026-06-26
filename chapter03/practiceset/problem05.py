#wap in python to  fromat the following letter using esccape  sequence  character
letter = "hello himanshi!"
# \n -> New Line
text = "Hello\nHimanshi"
print(text)

# \t -> Tab Space
text = "Hello\tHimanshi"
print(text)

# \\ -> Print a Backslash
text = "C:\\Users\\Himanshi"
print(text)

# \' -> Single Quote inside string
text = 'It\'s a beautiful day'
print(text)

# \" -> Double Quote inside string
text = "She said, \"Hello!\""
print(text)

# \b -> Backspace (removes previous character)
text = "Helloo\b"
print(text)

# \r -> Carriage Return (starts from beginning of line)
text = "Hello\rHi"
print(text)

# \f -> Form Feed
text = "Hello\fHimanshi"
print(text)

# \v -> Vertical Tab
text = "Hello\vHimanshi"
print(text)

# \a -> Alert/Bell sound (may not work in all terminals)
text = "Hello\a"
print(text)