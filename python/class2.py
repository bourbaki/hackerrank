from math import acos, degrees, sqrt

class Vector3D(object):
    """3D Vector in Euclidian Space"""
    def __init__(self, x, y, z):
        super(Vector3D, self).__init__()
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __pow__(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)
        
    def __abs__(self):
        return sqrt(self * self)
        
    def __xor__(self, other):
        # cosine
        return (self * other) / abs(self) / abs(other)
        
if __name__ == '__main__':
    tuples = (tuple(map(float, input().strip().split())) for _ in range(4))
    a, b, c, d = [Vector3D(*t) for t in tuples]
    ab, bc, cd = b - a, c - b, d - c
    x, y = ab ** bc, bc ** cd
    print("{:.2f}".format(degrees(acos(x ^ y))))
    