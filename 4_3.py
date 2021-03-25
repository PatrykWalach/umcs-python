class LiczbaZespolona(complex):
    def modul(self):
        return abs(self)

    def __str__(self):
        return '('+str(self.real)+','+str(self.imag)+')'

    def __add__(self, other):
        return LiczbaZespolona(super().__add__(other))

    def __mul__(self, other):
        return LiczbaZespolona(super().__mul__(other))

    def __sub__(self, other):
        return LiczbaZespolona(super().__sub__(other))

    def __truediv__(self, other):
        return LiczbaZespolona(super().__truediv__(other))


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
