# detailed_output.py
def detailed_message(num1: int, num2: int, num3: int) -> str:
    largest = num1
    var_name = "num1"

    if num2 >= largest:
        largest = num2
        var_name = "num2"
        if num3 >= largest:
            largest = num3
            var_name = "num3"
    else:
        if num3 >= largest:
            largest = num3
            var_name = "num3"

    return (
        "Message to User: You entered three numbers, "
        f"{num1}, {num2}, and {num3}. The first whole number you entered "
        "was assigned to a variable named num1, the second "
        f"({num2}) to num2, and finally the third ({num3}) was assigned "
        f"to num3. Your input was processed and the largest number you "
        f"entered was {largest}, which belonged to an integer variable "
        f"named {var_name}."
    )

if __name__ == "__main__":
    n1 = int(input("Enter first integer (num1): "))
    n2 = int(input("Enter second integer (num2): "))
    n3 = int(input("Enter third integer (num3): "))
    print(detailed_message(n1, n2, n3))
