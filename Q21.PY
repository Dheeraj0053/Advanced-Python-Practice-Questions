def moveZeros(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]

print(moveZeros([1, 2, 0, 4, 0, 5, 0]))  # [1, 2, 4, 5, 0, 0, 0]