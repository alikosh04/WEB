#problem a
n = int(input())
i = 2

while n % i != 0:
    i += 1

print(i)
#problem b
n = int(input())
i = 1

while i * i <= n:
    print(i * i, end=" ")
    i += 1
#problem c
n = int(input())
i = 1

while i * i <= n:
    print(i * i, end=" ")
    i += 1
#problem d
n = int(input())
curr = 1

while curr < n:
    curr *= 2

if curr == n:
    print("YES")
else:
    print("NO")
#problem e
n = int(input())
k = 0
curr = 1

while curr < n:
    curr *= 2
    k += 1

print(k)