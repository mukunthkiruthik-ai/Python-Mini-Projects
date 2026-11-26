"""
🧮 Unit Converter
Convert between various units of measurement
Author: Mukunth Kiruthik R S | B.Tech AI&DS, KPRIET
"""

def temperature_converter():
    """Convert between Celsius, Fahrenheit, and Kelvin"""
    print("\n🌡️  Temperature Converter")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    
    choice = input("Choice: ")
    value = float(input("Enter value: "))
    
    conversions = {
        "1": (lambda v: v * 9/5 + 32, "°C", "°F"),
        "2": (lambda v: (v - 32) * 5/9, "°F", "°C"),
        "3": (lambda v: v + 273.15, "°C", "K"),
        "4": (lambda v: v - 273.15, "K", "°C"),
    }
    
    if choice in conversions:
        func, from_unit, to_unit = conversions[choice]
        result = func(value)
        print(f"✅ {value}{from_unit} = {result:.2f}{to_unit}")
    else:
        print("Invalid choice!")

def length_converter():
    """Convert between length units"""
    print("\n📏 Length Converter")
    print("1. Meters → Feet")
    print("2. Feet → Meters")
    print("3. Kilometers → Miles")
    print("4. Miles → Kilometers")
    print("5. Centimeters → Inches")
    print("6. Inches → Centimeters")
    
    choice = input("Choice: ")
    value = float(input("Enter value: "))
    
    conversions = {
        "1": (lambda v: v * 3.28084, "m", "ft"),
        "2": (lambda v: v / 3.28084, "ft", "m"),
        "3": (lambda v: v * 0.621371, "km", "mi"),
        "4": (lambda v: v / 0.621371, "mi", "km"),
        "5": (lambda v: v / 2.54, "cm", "in"),
        "6": (lambda v: v * 2.54, "in", "cm"),
    }
    
    if choice in conversions:
        func, from_unit, to_unit = conversions[choice]
        result = func(value)
        print(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

def weight_converter():
    """Convert between weight units"""
    print("\n⚖️  Weight Converter")
    print("1. Kilograms → Pounds")
    print("2. Pounds → Kilograms")
    print("3. Grams → Ounces")
    print("4. Ounces → Grams")
    
    choice = input("Choice: ")
    value = float(input("Enter value: "))
    
    conversions = {
        "1": (lambda v: v * 2.20462, "kg", "lbs"),
        "2": (lambda v: v / 2.20462, "lbs", "kg"),
        "3": (lambda v: v * 0.035274, "g", "oz"),
        "4": (lambda v: v / 0.035274, "oz", "g"),
    }
    
    if choice in conversions:
        func, from_unit, to_unit = conversions[choice]
        result = func(value)
        print(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

def main():
    print("=" * 40)
    print("🧮 UNIVERSAL UNIT CONVERTER")
    print("=" * 40)
    
    while True:
        print("\nCategories:")
        print("1. 🌡️  Temperature")
        print("2. 📏 Length")
        print("3. ⚖️  Weight")
        print("4. ❌ Exit")
        
        category = input("\nSelect category (1-4): ")
        
        if category == "1":
            temperature_converter()
        elif category == "2":
            length_converter()
        elif category == "3":
            weight_converter()
        elif category == "4":
            print("\nGoodbye! 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
