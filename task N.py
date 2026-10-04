n = int(input())

minutes = 9 * 60 + n * 45 + (n - 1) // 2 * 5 + n // 2 * 15

print(minutes // 60, minutes % 60)
