def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
   
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (Celsius or Fahrenheit): ").lower()

    if unit == 'celsius':
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature} degrees Celsius is {converted_temperature:.2f} degrees Fahrenheit.")
    elif unit == 'fahrenheit':
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature} degrees Fahrenheit is {converted_temperature:.2f} degrees Celsius.")
    else:
        print("Error: Invalid unit of measurement. Please enter 'Celsius' or 'Fahrenheit'.")

temperature_converter()
