hrs = float(input("Enter Hours:"))
rte = float(input("Enter Rate:"))

pay = hrs * rte

if hrs > 40:
    pay += (hrs - 40) * rte * 0.5

print(pay)
