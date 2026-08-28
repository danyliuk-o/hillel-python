lst = [0, 1, 0, 12, 3]

new_lst = []
zero_count = 0

for item in lst:
    if item != 0:
        new_lst.append(item)
    else:
        zero_count += 1

new_lst += [0] * zero_count


print("list -> ", new_lst)