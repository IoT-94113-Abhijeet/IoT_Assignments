# main.py

# Import specific modules from the package
from airthmetic import add,multiply
from string import reverse_string, count_vowels

# Demonstrate arithmetic functions
a = 10
b = 5
print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))

# Demonstrate string functions
text = "Hello World"
print("Original String:", text)
print("Reversed String:", reverse_string(text))
print("Number of Vowels:", count_vowels(text))
