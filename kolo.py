import random

m = ['***', '**_', '*_*', '*__', '_**', '_*_', '__*', '___']

rule = [0, 1, 0, 1, 1, 0, 1, 0]


def automat(rule, n, k, plik):
    result = [{
        True: '*',
        False: '_'
    }[random.random() > 0.5] for i in range(n)]

    nextResult = result.copy()
    for i in range(k):
        for j in range(len(result)):
            nextResult[j-1] = {
                1: '*',
                0: '_'
            }[rule[m.index(''.join(result[j-2]+result[j-1]+result[j]))]]
        result = nextResult

    with open(plik, 'w') as f:
        f.write(''.join(result))


automat(rule, 5, 1, 'kolo-t.txt')
