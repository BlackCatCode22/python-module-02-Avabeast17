# largest_of_3.py
num1 = int(input("Enter first integer (num1): "))
num2 = int(input("Enter second integer (num2): "))
num3 = int(input("Enter third integer (num3): "))

# strictly nested decisions (no max(), no sorting)
largest = num1
if num2 >= largest:
    largest = num2
    if num3 >= largest:
        largest = num3
else:
    if num3 >= largest:
        largest = num3

print(f"Largest number: {largest}")
