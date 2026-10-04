a = int(input())
b = int(input())

d = a - b
k = (d // 1000) * 2 + 1
print((a + b + d * k) // 2)
