#problem a

a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)


#problem b

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")


#problem c

ans_sys = int(input())
ans_user = int(input())

if (ans_sys == 1 and ans_user == 1) or (ans_sys != 1 and ans_user != 1):
    print("YES")
else:
    print("NO")


#problem d
x = int(input())

if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#problem e

a = int(input())
b = int(input())

if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)