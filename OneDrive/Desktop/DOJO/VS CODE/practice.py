
# amount = float(input())


# if amount >= 500:
#     discount = 20
# elif amount >= 300:
#     discount = 15
# elif amount >= 200:
#     discount = 10
# else:
#     discount = 0


# final_amount = amount - (amount * discount / 100)


# print(f"Discount: {discount}%")
# print(f"Final Amount: {final_amount:.2f}")

# # Input: number of hours worked in a week
# hoursWorked = int(input().strip())

# # Pay calculation
# if hoursWorked <= 40:
#     totalPay = hoursWorked * 15.00
# elif hoursWorked <= 60:
#     totalPay = (40 * 15.00) + ((hoursWorked - 40) * 22.50)
# else:
#     totalPay = (40 * 15.00) + (20 * 22.50) + ((hoursWorked - 60) * 30.00)

# # Output: total weekly pay formatted to 2 decimal places
# print(f"{totalPay:.2f}")


# a = float(input())
# b = float(input())

# c = a * ( b / 100)

# print(f" {c:.2f}")



# n = int(input())
# a = list(map(int, input().split()))
# a.sort(key=lambda x: (sum(map(int, str(x))), x))
# print(*a) 



# import math
# a, b = list(map(int, input().split()))
# g = math.gcd(a, b)
# print(f"{a//g}/{b//g}")



# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)
# h = int(input())
# for i in range(h):
#     print(fib(i), end=" ")



# def pent(n):

#     return n * (3 * n - 1) // 2
# n = int(input())
# for i in range(1, n + 1):
#     print(pent(i), end=" ")


