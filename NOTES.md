# Study Notes
 
Daily notes from my Python backend study plan (16/11/2026 – 05/01/2027).
Background: Java + Spring Boot, new to Python.
 
## Improvements Backlog
 
Ideas to come back to as I learn new topics. Tick them off when done.
 
- [ ] **Day 5 (functions):** refactor the temperature converter to convert any unit to Celsius first, then to the target unit, using a dict of functions instead of one `match` case per unit pair
- [ ] **Day 5 (functions):** add Fahrenheit ↔ Kelvin conversions (comes for free with the Celsius approach)
- [ ] **Day 9 (exceptions):** handle invalid temperature input (e.g. `abc`) with `try/except ValueError` instead of crashing
- [ ] **Day 9 (exceptions):** show the real `ValueError` / `TypeError` messages in `dia01_tipos.py` instead of hard-coded text
- [ ] **Day 11 (pytest):** write tests for the conversion formulas
---
 
## Day 1 – 16/11/2026 · Environment + basic types
 
### What I built
- Project setup: `python-fundamentos` repo, virtual environment (`.venv`) and `.gitignore`
- `semana1/dia01_tipos.py`: a script that prints and explains Python's basic types when run
- `semana1/temperature_converter.py`: temperature converter (Celsius, Fahrenheit, Kelvin) with a menu using `match`
### Key learnings
- **Dynamic but strong typing:** the *value* has a type, not the variable. A variable can point to an `int` and later to a `str`. But Python never silently mixes types: `"5" + 3` raises `TypeError`.
- **Division:** `/` always returns a `float` (`10 / 3 = 3.33...`); `//` is integer division (`10 // 3 = 3`).
- **`int` has no size limit:** no overflow, no need for `long` or `BigInteger`.
- **`input()` always returns a `str`:** numbers must be converted with `int()` or `float()`.
- **Indentation is syntax:** blocks are defined by 4 spaces and `:`, not by `{}`.
- **Self-documenting f-strings:** `f"{10 / 3 = }"` prints both the expression and the result, so the explanation never gets out of sync with the code.
- **`match` / `case`** (Python 3.10+) is the closest thing to Java's `switch`: no `break`, no fall-through, and `case _:` is the default.
### Java vs Python
 
| Java | Python |
| --- | --- |
| `int age = 25;` | `age = 25` |
| `true` / `false` / `null` | `True` / `False` / `None` |
| `&&` / `\|\|` / `!` | `and` / `or` / `not` |
| `name.length()` | `len(name)` |
| `String.format("%.2f", x)` | `f"{x:.2f}"` |
| `"5" + 3` → `"53"` | `"5" + 3` → `TypeError` |
| `switch` + `default` | `match` + `case _:` |
| `camelCase` | `snake_case` |
 
### Where I got stuck
 
| Problem | Cause | Fix |
| --- | --- | --- |
| `match` never reached the right `case` | I wrote `match value` (the temperature, a `float`) instead of `match option` | Match on the variable that holds the menu choice |
 
### Questions to revisit
- When should I validate input *before* the `match` instead of using `case _`?
---
 
## Day 2 – 17/11/2026 · Strings and control flow
 
### What I built
-
### Key learnings
-
### Java vs Python
 
| Java | Python |
| --- | --- |
| | |
 
### Where I got stuck
 
| Problem | Cause | Fix |
| --- | --- | --- |
| | | |
 
### Questions to revisit
-