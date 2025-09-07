# work_ex_3_1.py
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    regular = 40 * rate
    overtime = (hours - 40) * rate * 1.5
    pay = regular + overtime
else:
    pay = hours * rate

print(f"Pay: ${pay:.2f}")
