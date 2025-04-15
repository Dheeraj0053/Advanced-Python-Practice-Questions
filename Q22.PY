class DimensionMismatchException(Exception):
    pass

def printMat(matrix):
    n = int(len(matrix) ** 0.5)
    if n * n != len(matrix):
        raise DimensionMismatchException("Matrix dimensions must be square.")
    for i in range(n):
        print("  ".join(map(str, matrix[i*n:(i+1)*n])))

printMat([1, 2, 0, 4, 0, 5, 0, 7, 9])
# Output:
# 1  2  0
# 4  0  5
# 0  7  9