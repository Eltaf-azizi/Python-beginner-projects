def length_converter(value, from_unit, to_unit):
    units = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }
    return value * units[from_unit] / units[to_unit]

def weight_converter(value, from_unit, to_unit):
    units = {
        "gram": 1,
        "kilogram": 1000,
        "milligram": 0.001,
        "pound": 453.592,
        "ounce": 28.3495
    }
    return value * units[from_unit] / units[to_unit]

def volume_converter(value, from_unit, to_unit):
    units = {
        "liter": 1,
        "milliliter": 0.001,
        "cubic_meter": 1000,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588
    }
    return value * units[from_unit] / units[to_unit]

def main():
    print("Welcome to the Unit Converter!")
    print("Choose the conversion type:")
    print("1. Length")
    print("2. Weight")
    print("3. Volume")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        value = float(input("Enter the value: "))
        from_unit = input("Enter the unit to convert from: ").lower()
        to_unit = input("Enter the unit to convert to: ").lower()
        result = length_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")

    elif choice == 2:
        value = float(input("Enter the value: "))
        from_unit = input("Enter the unit to convert from: ").lower()
        to_unit = input("Enter the unit to convert to: ").lower()
        result = weight_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")

    elif choice == 3:
        value = float(input("Enter the value: "))
        from_unit = input("Enter the unit to convert from: ").lower()
        to_unit = input("Enter the unit to convert to: ").lower()
        result = volume_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
