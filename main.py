## Repetitive Structures
# Exercise 2: Vowel Counter in a String
text = input("Enter a string: ").lower()

vowel_count = 0
vowels = set("aeiou")

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"The number of vowels in the string is: {vowel_count}")


