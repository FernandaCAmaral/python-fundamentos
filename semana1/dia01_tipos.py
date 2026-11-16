print("===== Week 1, Day 01 - Types =====")

# DYNAMIC TYPING
print("\n→ DYNAMIC TYPING")
age = 25
print(f"{age = } | type: {type(age)}")

age = "twenty"
print(f"\n{age = } | type: {type(age)}")

print("""
- In Python, the value has a type, not the variable.
A variable is just a name pointing to a value, and it can later point
to a value of a different type. This is flexible, but it also lets
bugs through that the Java compiler would catch.""")

# NUMBERS
print("\n→ NUMBERS")
print("Regular division always returns a float:")
print(f"{10 / 3 = }")
print("Integer division:")
print(f"{10 // 3 = }")

print("""
- Python's `int` has no size limit. 
There is no `long` type and no overflow; it functions like an automatic BigInteger.""")

# STRINGS
print("\n→ STRINGS")
name = "Fernanda"
print(f"{name = } | type: {type(name)} | lenght: {len(name)}")

print("""
- In Python, there is no char type. A character is simply a string of length 1.
- Just as in Java, `str` is immutable: `name.upper()` returns a new string and does not modify `name`.
- len() is a “standalone” function, not a method. 
This is a pattern in Python: len() works the same way for strings, lists, dictionaries, and other types.""")

# TYPE CONVERSIONS
print("\n→ TYPE CONVERSIONS")
print(f"{int('42') = }")
print(f"{float('3.5') = }")
print(f"{str(42) = }")
# These lines would crash the script, so they are shown as text only.
print("int('abc') -> ValueError")
print("'5' + 3 -> TypeError")

print("""
- In Java, "5" + 3 becomes "53" without any complaint. 
Python does not automatically convert types in this case and instead raises an error. 
In other words, while the typing is dynamic, it is also strong: it never silently mixes types.""")

