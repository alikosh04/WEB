#problem a
import math

a = int(input())
b = int(input())

c = (a**2 + b**2)**0.5

print(c)

#problem b
n = int(input())

print(f"The next number for the number {n} is {n + 1}.")
print(f"The previous number for the number {n} is {n - 1}.")


#problem c
n = int(input())
k = int(input())

result = k // n

print(result)



#problem d
n = int(input())
k = int(input())

ostatok = k % n

print(ostatok)



#problem e

v = int(input())
t = int(input())

position = (v * t) % 109

print(position)