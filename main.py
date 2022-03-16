# make a celsius to fahrenheit converter: need to write a function that takes a celsius value and returns the corresponding fahrenheit value

# defined the celsius value as an input and transformed it into an integer
# used error handling
while True:
    try:
        value_celsius = int(input("what's the temperature today in celsius? "))
        break
    except ValueError:
        print("Please insert a number")


# the equation used to calculate a fahrenheit value is 9/5 * celsius + 32. Convert the total value to an integer so we won't end upt with loads of decimal values
def converter(value_celsius):
    return int((9/5 * value_celsius + 32))


print(f"the temperature today is {converter(value_celsius)} fharenheit")
