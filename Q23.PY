class DimensionMismatchException(Exception):
    pass

def matMul(mat1, mat2):
    n = int(len(mat1) ** 0.5)
    if n * n != len(mat1) or len(mat1) != len(mat2):
        raise DimensionMismatchException("Matrices must be square and of equal size.")
    result = []
    for i in range(n):
        for j in range(n):
            result.append(sum(mat1[i*n + k] * mat2[k*n + j] for k in range(n)))
    return result

print(matMul([1, 2, 0, 4, 0, 5, 0, 7, 9], [1, 2, 0, 4, 0, 5, 0, 7, 9]))  
