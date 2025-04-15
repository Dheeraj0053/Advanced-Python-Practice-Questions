class LengthMismatchException(Exception):
    pass

def weave(lst1, lst2):
    if len(lst1) != len(lst2):
        raise LengthMismatchException("Lists must be of equal length.")
    result = []
    for a, b in zip(lst1, lst2):
        result.append(a)
        result.append(b)
    return result

print(weave([], []))          
print(weave([1, 2, 3], [4, 5, 6]))  
# print(weave([1, 2], [3]))   # IT WILL Raise LengthMismatchException