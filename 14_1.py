import time
import locale

locale.setlocale(locale.LC_ALL, 'pl_PL')


print(time.strftime(
    "Dzisiaj jest %A, %e %B %Y roku, godzina %H minut %M.", time.localtime()))


m = time.strptime("11 marzec 2020", "%d %B %Y")
c = time.strptime("3 czerwiec 2020", "%d %B %Y")
d = time.mktime(c)-time.mktime(m)
print(d//3600)


print(time.strftime("%A", time.strptime("16 październik 1978", "%d %B %Y")))
