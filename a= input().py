def selfnum(x):
    num = x
    for j in range(7):
        num = num+x % 10
        x = x//10
    return num


a = int(input())
min = 1000000

for i in range(a, a-55, -1):
    temp = selfnum(i)

    if temp == a and i < min:
        ans = i
        min = i

    if i == 1:
        break

if min != 1000000:
    print(min)
else:
    print("0")
