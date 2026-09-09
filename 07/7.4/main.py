def common_elements():
    multiples_of_3 = [x for x in range(0, 100, 3)]
    multiples_of_5 = [x for x in range(0, 100, 5)]

    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)

    return set_3 & set_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK!")