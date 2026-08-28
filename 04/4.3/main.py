import random

list_size = random.randint(3, 10)
original_list = [random.randint(1, 100) for _ in range(list_size)]

print("=" * 50)
print("Original list:", original_list)
print("=" * 50)

result = [original_list[0], original_list[2], original_list[-2]]

print("Result:", result)