'''
Algoritmo de Euclides.
Manuel Alejandro Martínez Flores
'''
def alg(a, b):
    '''
        Implementa algoritmo de Euclides para MCD
    '''
    if a < b :
        tmp = b
        b = a 
        a = tmp
        
    q = a // b
    r = a - b * q 
    
    if r == 0:
        return b 
    else :
        return alg(b, r)
    
    
    
    
while True :
    try :
        print ("a:")
        a = int(input())
        assert a > 0
        print ("b:")
        b = int(input())
        assert b > 0
        break
    except :
        pass 
 
    
print("MCD: ", alg(a,b))