lst = [1, 2]

half_len = (len(lst) + 1) // 2  #middle for odd
result = [lst[:half_len], lst[half_len:]]

print("list -> ", result)