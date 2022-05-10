
def euclide_ext_alg(a, b):
    '''
        as + bt = gcd(a, b)
    '''
    swap = b > a
    if swap :
        t = b 
        b = a
        a = t
        
    table = []
    table.append({'r' : a,
                  'q' : 0,
                  's' : 1,
                  't' : 0})
    q = a // b
    r = a - q * b
    table.append({'r' : b,
                  'q' : q,
                  's' : 0,
                  't' : 1})
    table.append({'r' : r})

    dlast = table[-1]
    while dlast['r'] != 0:
        a = table[-2]['r'] 
        b = dlast['r']
        q  = a // b
        r = a - q * b
        dlast['q'] = q 
        dlast['s'] = table[-3]['s'] - table[-2]['q'] * table[-2]['s']
        dlast['t'] = table[-3]['t'] - table[-2]['q'] * table[-2]['t']
        dlast = {'r' : r}
        table.append(dlast)
        
    if swap: 
        return table[-2]['t'], table[-2]['s']
    return table[-2]['s'], table[-2]['t']


    
def euclid_alg(a, b):
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
        return euclid_alg(b, r)
    
    
if __name__ == '__main__':    
    import random

    r = random.Random()
    for _ in range(1000):
        a = r.randint(4, 1000)
        b = r.randint(4, 1000)
        s, t = euclide_ext_alg(a, b)
        gcd = euclid_alg(a, b)
        assert a * s + b * t == gcd
