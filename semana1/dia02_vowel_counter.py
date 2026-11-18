print("===== VOWEL COUNTER =====")
text = input("Type a sentence: ")

vowels = "aeiouáàâãéèêíìîóòôõúùû"
counter = 0

for letter in text.lower():
    if letter in vowels:
        counter += 1

print(f"Your sentence has {counter} vowels")