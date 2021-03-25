
import re


WEIGHTS = [9, 7, 3, 1]*3

with open('5_4.txt') as f:
    for l in [l.strip()for l in f]:
        m = re.match(r'((\d{2})(\d{2})(\d{2})\d{3}(\d))(\d)$', l)
        if(m is None):
            print(l+' : Niedozwolony znak lub niepoprawna długość!')
            continue

        c, year, month, day, sex, s = m.groups()

        if(sum(int(c)*WEIGHTS[i] for c, i in zip(c, range(len(c)))) % 10 != int(s)):
            print(m.group()+' : Niepoprawna suma konrtolna')
            continue

        year = '19'+year if int(month) < 20 else '20'+year
        month = month if int(month) < 20 else str(
            int(month[:1])-2)+month[1]

        print(m.group()+' : ' + '-'.join([day, month, year]) +
              ' ' + ('mezczyzna' if int(sex) % 2 else 'kobieta'))
