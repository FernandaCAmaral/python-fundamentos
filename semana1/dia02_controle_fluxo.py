print("===== Week 1, Day 02 - Control Flow =====")

# IF/ELIF/ELSE
print("\n→ IF/ELIF/ELSE")
grade = 7.5

print(f"{grade = }")
if grade >= 9:
    print("Excellent")
elif grade >= 7:
    print("Approved")
else:
    print("Failed")

print("""
- Python allows chained comparisons, just like in mathematics:""")

age = 20
print(f"{age = }")
print(f"{18 <= age < 65 = }")   # True

# TRUTHINESS
print("\n→ TRUTHINESS")
print("""- In Python, any value can be used in an `if` statement, and the following are considered false:""")

print(f"{bool('') = }   | empty string")
print(f"{bool(0) = }    | zero")
print(f"{bool(None) = } | None")
print(f"{bool('abc') = } | not empty string")

print("""
- That's why, in Python, it is written as `if not ___`. 
In Java, you would write `if (___.isEmpty())`.
\nExample:
name = ""
if not name:
    print("Name is required.")   # runs, because "" is falsy""")
name = ""
if not name:
    print("Name is required.")

# FOR + RANGE
print("\n→ 'FOR' AND 'RANGE'")
word = "Python"
print(f"{word = }")
print("for letter in word:\n    print(letter)")

for letter in word:
    print(letter)

print("""
- Python's `for` loop iterates over items, like Java's for-each.
To repeat using numbers, use `range`:""")

print("\nfor i in range(5):\n    print(i, end=' ')")
for i in range(5):          # 0, 1, 2, 3, 4  → 5 IS NOT included
    print(i, end=" ")
print()

print("\nfor i in range(1, 6):\n    print(i, end=' ')")
for i in range(1, 6):       # 1 to 5
    print(i, end=" ")
print()

print("\nfor i in range(0, 11, 2):\n    print(i, end=' ')")
for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10 → the step is 2
    print(i, end=" ")
print()

print("""
- range(1, 6) is equivalent to for (int i = 1; i < 6; i++). 
The rule is the same as for slicing: the end value is never included.""")

# WHILE, BREAK, CONTINUE
print("\n→ WHILE, BREAK, CONTINUE")
count = 3
print(f"{count = }")
print("""
while count > 0:
    print(count, end=' ')
    count -= 1
print("Go!")""")
while count > 0:
    print(count, end=" ")
    count -= 1
print("Go!")


print("""
for number in range(1, 11):
    if number == 7:
        break          
    if number % 2 == 0:
        continue      
    print(number)""")
for number in range(1, 11):
    if number == 7:
        break          # leaves the whole loop
    if number % 2 == 0:
        continue       # jumps to the next iteration
    print(number)      # prints 1, 3, 5

print("""
`break` and `continue` work exactly as they do in Java. 
The difference is that there are no `++` or `--` operators: use `+= 1` and `-= 1` instead.""")