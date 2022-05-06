'''
Manuel Alejandro Martínez Flores
Exponenciación en aritmética modular
'''

import numpy as np 


def power_bin(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza representacion binaria
    '''
    repr = np.base_repr(ex, base = 2)
    total = 1 
    b = b % n 
    
    for i in repr:
        if int(i):
            if b == 1 : return total
            if b == 0 : return 0 
            total = (total * b) % n 
        b = (b * b) % n 
    return total

assert power_bin(7, 45, 17) == 6 



def power_rec(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza recursión
    '''
    if ex == 0:
        return 1
    else:
        return (b * power_rec(b, ex - 1, n)) % n 
    
assert power_rec(7, 45, 17) == 6 



def power_rec2(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza recursión dividiendo por 2
    '''
    
    if ex == 0 :
        return 1
    if ex % 2 == 0:
        return power_rec(b, ex/2, n) ** 2 % n 
    else :
        return b * power_rec(b, (ex - 1)/2, n) ** 2 % n 
    
assert power_rec2(7, 45, 17) == 6 