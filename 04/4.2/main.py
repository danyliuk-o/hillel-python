lst = []

result = 0

if lst:
    result = sum(lst[::2]) * lst[-1]

print("Result:", result)
