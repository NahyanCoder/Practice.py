binary = input("Enter a binary number: ")
decimal = 0
power = 0

while binary !='':
    digit = int(binary[-1])  # Get the last digit
    decimal += digit * (2 ** power)
    binary = binary[:-1]  # Remove the last digit
    power += 1

print(f"The decimal equivalent is: {decimal}")
decimal_number = int(input("Enter a decimal number: "))
binary_representation = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_representation = str(remainder) + binary_representation
    decimal_number = decimal_number // 2

print("Binary representation:", binary_representation)