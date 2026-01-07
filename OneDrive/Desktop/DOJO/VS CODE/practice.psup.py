
amount = float(input())


if amount >= 500:
    discount = 20
elif amount >= 300:
    discount = 15
elif amount >= 200:
    discount = 10
else:
    discount = 0


final_amount = amount - (amount * discount / 100)


print(f"Discount: {discount}%")
print(f"Final Amount: {final_amount:.2f}")




amount = float(input())

if amount >= 500:
    discount = 20
elif amount >= 300:
    discount = 15
elif amount >= 200:
    discount = 10
else:
    discount = 0

final_amount = amount - ( amount * discount / 100)

print(f"Discount: {discount}%")
print(f"Final Amount: {final_amount:.2f}")






hoursWorked = int(input().strip())


if hoursWorked <= 40:
    totalPay = hoursWorked * 15.00
elif hoursWorked <= 60:
    totalPay = (40 * 15.00) + ((hoursWorked - 40) * 22.50)
else:
    totalPay = (40 * 15.00) + (20 * 22.50) + ((hoursWorked - 60) * 30.00)


print(f"{totalPay:.2f}")




n = int(input().strip())

if n <= 40:
    totalpay = n * 15.00
elif n <= 60:
    totalpay = (40 * 15.00) + ((n-40)*22.50)
else:
    totalpay = (40 * 15.00) + (20 * 22.50) +((n-60)*30.00)

print(f"{totalpay:.2f}")





a = int(input())   
c = 0

if a <= 10:
    c = a * 2
elif a <= 30:
    c = 10*2 + (a-10)*3.5
elif a <= 50:
    c = 10*2 + 20*3.5 + (a-30)*5
else:
    c = 10*2 + 20*3.5 + 20*5 + (a-50)*8

print(f"{c:.2f}")




a = int(input())
c = 0

if a <= 10:
    c = a*2
elif a <= 30:
    c = 10*2 + ((a-10)*3.5)
elif a <= 50:
    c = 10*2 + 20*3.5 + ((a-30)*5)
else:
    c = 10*2 + 20*3.5 + 20*5 ((a-50)*8)

print(f"{c:.2f}")





a = float(input())   
b = float(input())   

c = a / (b*b)
d = round(c, 1)

print(f"BMI: {d}")

if d < 18.5:
    print("Underweight")
elif d < 24.9:
    print("Normal weight")
elif d < 29.9:
    print("Overweight")
else:
    print("Obesity")



a = float(input())
b = float(input())

c = a / (b*b)
d = round(c, 1)

print(f"BMI: {d}")

if d < 18.5:
    print("Underweight")
elif d < 24.9:
    print("Normal weight")
elif d < 29.9:
    print("Overweight")
else:
    print("Obesity")




a = float(input())

if a <= 10:
    b = 5
elif a <= 20:
    b = 7.5
else:
    b = 10

print(f"{b:.2f}")




a = float(input())

if a <= 10:
    b = 5
elif a <= 20:
    b = 7.50
else:
    b = 10

print(f"{b:.2f}")





a = int(input())

if a >= 90:
    g, r = "A", "Excellent"
elif a >= 80:
    g, r = "B", "Very Good"
elif a >= 70:
    g, r = "C", "Good"
elif a >= 60:
    g, r = "D", "Satisfactory"
else:
    g, r = "F", "Needs Improvement"

print(g)
print(r)





a = int(input())

if a >= 90:
    g, r = "A", "Excellent"
elif a >= 80:
    g, r = "B", "Very Good"
elif a >= 70:
    g, r = "C", "Good"
elif a >= 60:
    g, r = "D", "Satisfactory"
else:
    g, r = "F", "Needs Improvement"

print(g)
print(r)









a = int(input())
b = 0

if a > 300:
    b = (a-300)*1.5 + 100*1.2 + 100*0.75 + 100*0.5
elif a > 200:
    b = (a-200)*1.2 + 100*0.75 + 100*0.5
elif a > 100:
    b = (a-100)*0.75 + 100*0.5
else:
    b = a * 0.5

print(f"{b:.2f}")
