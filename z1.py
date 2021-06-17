# miejsce na kod:
def dekorator(fun):
    def decorated(arg):
        if not isinstance(arg, str):
            return 'Bad input type!'
        return fun(arg)
    return decorated


# koniec

@dekorator
def koder(rstr):
    return ''.join([chr(ord(lit)+3) for lit in rstr])


print(koder('abcd'))
#wynik: 'defg'
print(koder(12))
#wynik: 'Bad input type!'
