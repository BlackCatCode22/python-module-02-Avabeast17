# work_ex_3_2.py
try:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
except ValueError:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    regular = 40 * rate
    overtime = (hours - 40) * rate * 1.5
    pay = regular + overtime
else:
    pay = hours * rate

print(f"Pay: ${pay:.2f}")
