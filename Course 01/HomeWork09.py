n = int(input())
x = int(input())

result = 0
for i in range(n):
    if x % 2 != 0:
        x = (x * 2) - 1
    else:
        x = x // 2

print(x)
