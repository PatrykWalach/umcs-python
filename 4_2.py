class A:
    def info(self):
        print('Klasa A')


class B:
    def info(self):
        print('Klasa B')


class C:
    def info(self):
        print('Klasa C')


class D(A, B, C):
    def info(self):
        print('Klasa D')
        super(D, self).info()
        super(A, self).info()
        super(B, self).info()


D_obj = D()
D_obj.info()
