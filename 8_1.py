
messages = {
    'pl': {
        0: 'zero', 1: 'jeden', 2: 'dwa',
        3: 'trzy', 4: 'cztery', 5: 'pięć',
        6: 'sześć', 7: 'siedem', 8: 'osiem', 9: 'dziewięć'
    }
}
locale = 'pl'


def result_to_locale(fn):
    def decorated(*args):
        r = fn(*args)
        return ' '.join(messages[locale][int(x)] for x in str(r))
    return decorated


@result_to_locale
def add(a, b):
    return a+b

@result_to_locale
def mul(a, b):
    return a*b


print(mul(12,12))
print(add(12,75))