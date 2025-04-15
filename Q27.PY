class Vector:
    def __init__(self, components):
        self._components = components
    
    def __str__(self):
        return f"{len(self._components)}-dimensional vector: {self._components}"
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be a number.")
        return Vector([x * scalar for x in self._components])
    
    __rmul__ = __mul__
    
    def __add__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same dimension.")
        return Vector([a + b for a, b in zip(self._components, other._components)])
    
    def __sub__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same dimension.")
        return Vector([a - b for a, b in zip(self._components, other._components)])
    
    def __matmul__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same dimension.")
        return sum(a * b for a, b in zip(self._components, other._components))

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1)         
print(2 * v1)     
print(v1 + v2)     
print(v1 - v2)     
print(v1 @ v2)     