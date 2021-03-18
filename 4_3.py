class LiczbaZespolona:
    def modul(self):
        return abs(self.value)

    def __str__(self):
        return '('+str(self.value.real)+','+str(self.value.imag)+')'

    def __add__(self, other):
        r = self.value+other.value
        return LiczbaZespolona(r.real, r.imag)

    def __mul__(self, other):
        r = self.value*other.value
        return LiczbaZespolona(r.real, r.imag)

    def __sub__(self, other):
        r = self.value-other.value
        return LiczbaZespolona(r.real, r.imag)

    def __truediv__(self, other):
        r = self.value/other.value
        return LiczbaZespolona(r.real, r.imag)

    def __init__(self, real, imaginary):
        self.value = complex(real, imaginary)


za = LiczbaZespolona(1, 1)
zb = LiczbaZespolona(2, 2)
print("za=%s" % za)
print("zb=%s" % zb)
print("%s+%s=%s" % (za, zb, (za+zb)))
print("%s-%s=%s" % (za, zb, (za-zb)))
print("%s*%s=%s" % (za, zb, (za*zb)))
print("modul(za) = %s" % (za.modul()))
print("modul(zb) = %s" % (zb.modul()))
print("%s/%s=%s" % (za, zb, (za/zb)))
