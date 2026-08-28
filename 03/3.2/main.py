lst = [1, 12, 100]

if (len(lst) > 1):
    lst = lst[-1:] + lst[:-1]

print("list -> ", lst)