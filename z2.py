# miejsce na kod:
factory = lambda shift: lambda fun: lambda string: ''.join([chr(i +shift) for i in fun(string)])
    
# koniec  

def fun(rstr):    
    return [ord(lit) for lit in rstr] 
    
koder=factory(3)(fun)
print(koder('abcd'))
#output: defg

dekoder=factory(-3)(fun)
print(dekoder('defg'))
#output:abcd    
    
   