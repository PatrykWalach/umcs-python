class AddMul:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return AddMul(self.value * other.value)

    def __add__(self, other):
        return AddMul(self.value + other.value)

    def __str__(self):
        return str(self.value)


a = AddMul(5)
b = AddMul(5)
c = a*b
print(c, type(c))
print(a+b, type(a+b))
