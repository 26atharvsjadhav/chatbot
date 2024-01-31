def length_conversion():
    print("Welcome to the Length Conversion Chatbot!")
    print("I can convert between different units of length.")

    while True:
        user_input = input("Enter a length (e.g., '5 meters'): ").split()

        if len(user_input) != 2:
            print("Invalid input. Please try again.")
            continue

        value, unit = float(user_input[0]), user_input[1].lower()

        if unit == 'meters':
            print(f"{value} meters is {value * 39.37} inches.")
        elif unit == 'inches':
            print(f"{value} inches is {value / 39.37} meters.")
        else:
            print("I can only convert between meters and inches.")

        another = input("Do you want to convert another length? (yes/no): ").lower()
        if another != 'yes':
            break

def weight_conversion():
    print("Welcome to the Weight Conversion Chatbot!")
    print("I can convert between different units of weight.")

    while True:
        user_input = input("Enter a weight (e.g., '5 kilograms'): ").split()

        if len(user_input) != 2:
            print("Invalid input. Please try again.")
            continue

        value, unit = float(user_input[0]), user_input[1].lower()

        if unit == 'kilograms':
            print(f"{value} kilograms is {value * 2.20462} pounds.")
        elif unit == 'pounds':
            print(f"{value} pounds is {value / 2.20462} kilograms.")
        else:
            print("I can only convert between kilograms and pounds.")

        another = input("Do you want to convert another weight? (yes/no): ").lower()
        if another != 'yes':
            break

def temperature_conversion():
    print("Welcome to the Temperature Conversion Chatbot!")
    print("I can convert between Celsius and Fahrenheit.")

    while True:
        user_input = input("Enter a temperature (e.g., '25 Celsius'): ").split()

        if len(user_input) != 2:
            print("Invalid input. Please try again.")
            continue

        value, unit = float(user_input[0]), user_input[1].lower()

        if unit == 'celsius':
            fahrenheit = (value * 9/5) + 32
            print(f"{value} Celsius is {fahrenheit} Fahrenheit.")
        elif unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
            print(f"{value} Fahrenheit is {celsius} Celsius.")
        else:
            print("I can only convert between Celsius and Fahrenheit.")

        another = input("Do you want to convert another temperature? (yes/no): ").lower()
        if another != 'yes':
            break

# Main program
print("Welcome to the Unit Conversion Chatbot!")
while True:
    print("\nChoose a conversion type:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        length_conversion()
    elif choice == '2':
        weight_conversion()
    elif choice == '3':
        temperature_conversion()
    elif choice == '4':
        print("Goodbye! Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")
