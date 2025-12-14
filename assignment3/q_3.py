def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

def count_consonants(s):
    return sum(1 for ch in s if ch.isalpha() and ch not in "aeiouAEIOU")

def vowel_consonant_ratio(s):
    v = count_vowels(s)
    c = count_consonants(s)
    return v / c if c != 0 else 0

text = input("Enter a string: ")

print("Vowels:", count_vowels(text))
print("Consonants:", count_consonants(text))
print("Vowel to Consonant Ratio:", vowel_consonant_ratio(text))
