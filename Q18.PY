def delDup(lst):
    seen = []
    result = []
    for num in lst:
        if num not in seen:
            seen.append(num)
            result.append(num)
    return result

print(delDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))  
print(delDup([-1, 1, -1, 8]))  