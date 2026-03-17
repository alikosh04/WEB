#problem a
n = int(input())
a = input().split()

for i in range(0, n, 2):
    print(a[i], end=" ")
#problem b
n = int(input())
a = list(map(int, input().split()))

for x in a:
    if x % 2 == 0:
        print(x, end=" ")
#problem c
n = int(input())
a = list(map(int, input().split()))
count = 0

for x in a:
    if x > 0:
        count += 1

print(count)
#problem d 
n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(1, n):
    if a[i] > a[i-1]:
        count += 1

print(count)
#problem e
n = int(input())
a = list(map(int, input().split()))
found = False

for i in range(1, n):
    if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
#problem f 
n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(1, n - 1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        count += 1

print(count)
#problem g
n = int(input())
a = input().split()

print(*(a[::-1]))