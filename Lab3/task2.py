def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius*9/5) + 32
  return fahrenheit

celsius = float(input("\nEnter temperature in celsius:  "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

fahrenheit = float(input("Enter temperature in fahrenheit:  "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°C is equal to {celsius}°C")