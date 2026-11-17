print("=== Temperature Converter ===")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("3 - Celsius to Kelvin")
print("4 - Kelvin to Celsius")

option = input("Choose an option: ").strip()

if option not in ["1", "2", "3", "4"]:
    print("Invalid option. Please choose 1, 2, 3 or 4.")
else:
    value = float(input("Enter a temperature: ").replace(",", "."))

    match option:
        case "1":
            result = value * 9 / 5 + 32
            print(f"{value:.2f} Celsius is {result:.2f} Fahrenheit")
        case "2":
            result = (value - 32) * 5 / 9
            print(f"{value:.2f} Fahrenheit is {result:.2f} Celsius")
        case "3":
            result = value + 273.15
            print(f"{value:.2f} Celsius is {result:.2f} Kelvin")
        case "4":
            result = value - 273.15
            print(f"{value:.2f} Kelvin is {result:.2f} Celsius")