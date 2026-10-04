n = int(input())
k = int(input())

r = k % n
print((n - r) * (r != 0))
