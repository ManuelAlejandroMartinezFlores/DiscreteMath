'''
Manuel Alejandro Martínez Flores
Exponenciación en aritmética modular
'''


def power_bin(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza representacion binaria
    '''
    repr = bin(ex)[2:]
    total = 1 
    b = b % n 
    
    for i in repr[::-1]:
        if int(i):
            if b == 1 : return total
            if b == 0 : return 0 
            total = (total * b) % n 
        b = (b * b) % n 
    return total



def power_rec(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza recursión
    '''
    if ex == 0:
        return 1
    else:
        return (b * power_rec(b, ex - 1, n)) % n 
    



def power_rec2(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza recursión dividiendo por 2
    '''
    
    if ex == 0 :
        return 1
    if ex % 2 == 0:
        return power_rec2(b, ex/2, n) ** 2 % n 
    else :
        return b * power_rec2(b, (ex - 1)/2, n) ** 2 % n 
    