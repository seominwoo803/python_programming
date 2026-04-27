class Vector :

    def __init__(self, x, y) :

        self.x = x
        self.y = y

    def __add__(self, other) :

        if isinstance(other, Vector) :

            return Vector(self.x + other.x, self.y + other.y)

        return NotImplemented

    def __radd__(self, other) :

        if isinstance(other, int) :

            return Vector(self.x + other, self.y + other)

        return NotImplemented

    def __str__(self) :

        return f'({self.x}, {self.y})'

v = Vector(3, 4)

print(v)

v1 = Vector(4, 1)
v2 = Vector(2, 7)

print(v1 + v2)

vv = Vector(5, 6)
print(7 + vv)
