#problem a

a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

#problem b
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")
#problem c
a = int(input())
b = int(input())

for i in range(a, b + 1):
    root = i ** 0.5
    if root == int(root):
        print(i, end=" ")
#problem g
x = int(input())

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break
#problem h
x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")
#problem j
total = 0

for _ in range(100):
    total += int(input())

print(total)
#problem k
n = int(input())
total = 0

for _ in range(n):
    total += int(input())

print(total)
#problem m
n = int(input())
count = 0

for _ in range(n):
    if int(input()) == 0:
        count += 1

print(count)