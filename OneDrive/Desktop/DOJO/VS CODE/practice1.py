# n = int(input())
# arr = list(map(int, input().split()))

# f = s  = -10**18
# for i in arr:
#     if i > f:
#         s = f
#         f = i
#     elif i > s and i != f:
#         s = i 

# print(s) 


# n = int(input())
# a = list(map(int, input().split()))

# f = s = -10**18
# for i in a:
#     if i > f:
#         s = f
#         f = i
#     elif i > s and i != f:
#         s = i

# print(s)





# n = int(input().strip())
# arr = list(map(int, input().split()))

# a = True
# for i in range(n-1):
#     if arr[i] > arr[i+1]:
#         a = False
#         break

# if (a):
#     print(1)
# else:
#     print(0)


# n = int(input().strip())
# arr = list(map(int, input().split()))

# a = True
# for i in range(n-1):
#     if arr[i] > arr[i+1]:
#         a = False
#         break

# if (a):
#     print(1)
# else:
#     print(0)





# n = int(input().strip())
# arr = list(map(int, input().split()))[:n]

# even = []
# odd = []

# for i in arr:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(*even)
# print(*odd)




# n = int(input().strip())
# arr = list(map(int, input().split()))[:n]

# i, j = 0, n-1
# while i < j:
#     arr[i], arr[j] = arr[j], arr[i]
#     i += 1
#     j -= 1

# print(*arr)


# n = int(input().strip())
# arr = list(map(int, input().split()))[:n]

# i, j = 0 , n-1
# while i < j:
#     arr[i], arr[j] = arr[j], arr[i]
#     i += 1
#     j -= 1

# print(*arr)




# n = int(input())
# arr = list(map(int, input().split()))

# b = []
# s = 0

# for i in range(n):
#     s = s + arr[i]
#     b.append(s)

# print(*b)   


# n = int(input())
# arr = list(map(int, input().split()))

# b = []
# s = 0

# for i in range(n):
#     s = s + arr[i]
#     b.append(s)

# print(*b)   



# n = int(input())
# arr = list(map(int, input().split()))

# a = [0] * n

# a[n-1] = arr[n-1]
# for i in range(n-2, -1, -1):
#     a[i] = arr[i] + a[i+1]

# print(*a, end= ' ')

# n = int(input())
# arr = list(map(int, input().split()))

# a = [0] * n

# a[n-1] = arr[n-1]
# for i in range(n-2, -1, -1):
#     a[i] = arr[i] + a[i+1]

# print(*a, end= ' ')

  
# SELECTION SORT

# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n-1):
#     a = i
#     for j in range(i+1, n):
#         if arr[j] < arr[a]:
#             a = j
#     arr[i], arr[a] = arr[a], arr[i] 
    
# print(*arr) 



# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n-1):
#     a = i
#     for j in range(i+1, n):
#         if arr[j] < arr[a]:
#             a = j
#     arr[i], arr[a] = arr[a], arr[i]

# print(*arr) 


#    BUBBLE SORT

# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(*arr)


# n = int(input())
# arr = list(map(int, input().split()))

# for i  in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(*arr)


# INSERTION

# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(1, n):
#     key = arr[i]
#     j = i - 1
#     while j>=0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j -=1
#         arr[j+1] = key

# print(*arr)


# n = int(input())
# arr = list(map(int, input().split()))

# for i in range(1,n):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j -= 1
#         arr[j+1] = key

# print(*arr)




# s = input()

# a, b, c = 0

# for ch in s:
#     if ch.isalpha():
#         a += 1
#     elif ch.isdigit():
#         b += 1
#     else:
#         c += 1

# print(a, b, c)   



# word = input()
# reverse = word.swapcase()
# print(reverse)

# s = input()
# a = ""

# for ch in s:
#     if ch.islower():
#         a += ch.upper()
#     elif ch.isupper():
#         a += ch.lower()
#     else:
#         a += ch 
# print(a) 



# a = int(input())
# arr1 = list(map(int, input().split()))
# b = int(input())
# arr2 = list(map(int, input().split()))

# m = sorted(arr1 + arr2)
# print(*m)   




# s = input()

# start = 0
# while start < len(s) and s[start] == ' ':
#     start += 1

# end = len(s) - 1
# while end >= start and s[end] == ' ':
#     end -= 1

# print(s[start:end + 1])




# s = input()
# w = input()

# i = -1
# for j in range(len(s) - len(w) +1):
#     if s[j:j+len(w)] == w:
#         i = j
#         break

# if i != -1:
#     print(s[:i] + s[i+len(w):])
# else:
#     print(s)

# s = input()
# w = input()

# i= -1

# for  j in range(len(s) - len(w)+1):
#     if s[j:j+len(w)] == w:
#         i=j
#         break

# if i != -1:
#     print(s[:i] + s[i+len(w):])
# else:
#     print(s)           


# s = input().strip()
# w = input().strip()
# i = -1

# for j in range(len(s) - len(w) +1):
#     if s[j:j+len(w)] == w:
#         i=j

# if i != -1:
#     s = s[:i] + s[i+len(w):]

# print(s.strip())




# n = int(input())
# arr = list(map(int, input().split()))

# dup = []
# for i in arr:
#     if i not in dup:
#         dup.append(i)

# for i in dup:
#     print(i, end=" ")


# x,n = map(float,input().split())
# decimal = x**n

# print(f"{decimal :.2f}")


# x = float(input())
# n = int(input())

# def p(a, b):
#     if b == 0: return 1
#     if b < 0: return 1 / p(a, -b)
#     return a * p(a, b - 1)

# print(f"{p(x, n):.2f}")



# x = float(input())
# n = int(input())

# def p(a, b):
#     if b == 0: return 1
#     if b < 0: return 1 / p(a, -b)
#     return a * p(a, b -1)

# print(f"{p(x, n):.2f}")


# n = int(input())
# arr = list(map(int, input().split()))
# x = int(input())

# a = []
# b = []

# for i in arr:
#     if i > x:
#         a.append(i)
#     else:
#         b.append(i)

# print(*a)
# print(*b)




# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# for i in range(0, n, k):
#     arr[i:i+k] = reversed(arr[i:i+k])

# print(*arr)



# n, d = map(int, input().split())
# a = list(map(int, input().split()))

# d = d % n
# a = a[-d:] + a[:-d]
# print(*a)

