def kMax(lst, k):
    if k <= 0 or k > len(lst):
        raise ValueError("k must be between 1 and the length of the list.")
    return sorted(lst, reverse=True)[k-1]

print(kMax([10, 2, 4, 5, 7, 9], 1))  
print(kMax([10, 2, 4, 5, 7, 9], 2))  
print(kMax([10, 2, 4, 5, 7, 9], 3))  