import temperature_functions as j
c= float(input("enter the temprature in Celsius = "))
print(f"{c}°Celcius = {j.Celsius_Fahrenheit(c)}° Fahrenheit ")

c= float(input("enter the temprature in Celsius = "))
print(f"{c}°Celcius = {j.Celsius_Kelvin(c)}° Kelvin ")

f= float(input("enter the temprature in Fahrenheit = "))
print(f"{c}°Fahrenheit = {j.Fahrenheit_Celsius(f)}° Celsius ")

f= float(input("enter the temprature in Fahrenheit = "))
print(f"{c}°Fahrenheit = {j.Fahrenheit_Kelvin(c)}° Kelvin ")

k= float(input("enter the temprature in Kelvin = "))
print(f"{c}°Kelvin = {j.Kelvin_Celsius(k)}° Celsius ")

k= float(input("enter the temprature in Kelvin = "))
print(f"{c}°Kelvin = {j.Kelvin_Fahrenheit(k)}° Fahrenheit ")