# main.py

# Import specific modules from the package
from operations import arithmetic, string_ops

# Demonstrate arithmetic functions
a = 10
b = 5
print("Addition:", arithmetic.add(a, b))
print("Multiplication:", arithmetic.multiply(a, b))

# Demonstrate string functions
text = "Hello World"
print("Original String:", text)
print("Reversed String:", string_ops.reverse_string(text))
print("Number of Vowels:", string_ops.count_vowels(text))
