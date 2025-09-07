# work_ex_4_6.py
def comput_pay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    return hours * rate

if __name__ == "__main__":
    h = float(input("Enter hours worked: "))
    r = float(input("Enter hourly rate: "))
    print(f"Pay: ${comput_pay(h, r):.2f}")
