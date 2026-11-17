print("===== Week 1, Day 02 - Strings =====")

# MOST USED STRING METHODS
print("\n→ STRING METHODS")

text = " Hello, Python World "
print(f"{text = }")
print(f"{text.strip() = } | Remove any whitespace from both ends of a string")
print(f"{text.lower() = } | Transform the String to lower case")
print(f"{text.replace('World', 'Dev') = } | Replace an 'old' word with a 'new' word")
print(f"{text.count('o') = } | Counts how often a specific element appears in a sequence")
print(f"{text.find('Python') = } | Finds a specified substring within a string and return the index of its first occurrence") # returns -1 if not found

print("""
- In Python, you can chain method calls — such as `text.strip().lower()`
without any concerns, because each method returns a new string.""")

# OPERATOR IN
print("\n→ OPERATOR 'IN'")
print(f"{'Python' in text = }")    # True
print(f"{'java' in text = }")      # False

print("""
- 'in' is an operator, not a method. 
It works the same way for strings, lists, dictionaries, and sets""")

# SPLIT AND JOIN
print("\n→ 'SPLIT' AND 'JOIN'")
sentence = "learn python every day"
print(f"{sentence = }")
print(f"{sentence.split() = }")
words = sentence.split()
print(f"{words = }")
print(f"{'-'.join(words) = }")

print("""
- split() with no argument splits by any whitespace and returns a list.""")

#SLICING
print("\n→ SLICING")
word = "Python"
print(f"{word = }")
print(f"{word[0:3] = }")    # 'Pyt'  → index 0 to 3, WITHOUT including the 3
print(f"{word[2:] = }")     # 'thon' → index 2 to end
print(f"{word[:2] = }")     # 'Py'   → from the beginning to index 2
print(f"{word[-3:] = }")    # 'hon'  → the last 3 indexes
print(f"{word[::-1] = }")   # 'nohtyP' → reversed

print("""
- The format is [start:end:step], and the end is never included. 
A step of -1 travels the sequence in reverse, which is why [::-1] reverses the string.""")

#METHODS THAT RETURN TRUE OR FALSE
print("\n→ TRUE OR FALSE METHODS")
print(f"{'123'.isdigit() = }")     # True  → only digits
print(f"{'abc'.isalpha() = }")     # True  → only letters
print(f"{'A'.isupper() = }")       # True
print(f"{'a'.isupper() = }")       # False