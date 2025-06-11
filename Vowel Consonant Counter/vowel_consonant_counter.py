import string

vowels = {"a", "e", "i", "o", "u"}
consonant = set(string.ascii_lowercase) - vowels

sentence = "Hello!! My name is John.".lower()

vowels_count = 0
consonant_count = 0

for char in sentence:
    if char != " " and char not in string.punctuation:
        if char in vowels:
            vowels_count += 1
        elif char in consonant:
            consonant_count += 1

print(f"Vowels: {vowels_count}")
print(f"Consonant: {consonant_count}")