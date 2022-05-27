'''
Manuel Alejandro Martínez Flores
Encriptación RSA
'''

L_TO_N = {l:id for id, l in enumerate('abcdefghijklmnopqrstuvwxyz'.upper())}
N_TO_L = {id:l for id, l in enumerate('abcdefghijklmnopqrstuvwxyz'.upper())}

def hard_inverse(phi, e):
    for i in range(1, phi):
        if (e * i) % phi == 1:
            return i 
        
def text_to_ASCII(text):
    return [L_TO_N[x] for x in text]

def padd(ascii, n = 25):
    txt = str(ascii)
    return "0" * (len(str(n)) - len(txt)) + txt 

def get_coprime(phi, e=65637):
    if e > phi:
        e = 33
    if euclid_alg(phi, e) == 1:
        return e 
    else:
        return get_coprime(phi, e + 2)
    
def get_unit_size(n):
    for i in range(1, 100):
        if int('25' * i) > n :
            return  i - 1
    
def ascii_to_unit(data, unit_size):
    result = []
    if len(data) % unit_size != 0 :
        data = data + ['0'* 2] * (unit_size - len(data) % unit_size)
    
    for i in range(len(data)// unit_size):
        result.append("".join(data[unit_size * i : unit_size * (i + 1)]))
    return result 

def unit_to_ascii(data, unit_size):
    result = []
    for x in data:
        # x = x[unit_size - len(x) % unit_size : ]
        for i in range(len(x) // 2):
            result.append(x[2 * i : 2 * (i + 1)])
    return result

def ascii_to_text(id):
    return N_TO_L[id]



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
    
def mpow(b, ex, n):
    '''
        b ^ ex (mod n)
        Utiliza recursión dividiendo por 2
    '''
    
    if ex == 0 :
        return 1
    if ex % 2 == 0:
        return mpow(b, ex/2, n) ** 2 % n 
    else :
        return b * mpow(b, (ex - 1)/2, n) ** 2 % n 
    
    
class DecoderRSA:
    def __init__(self, p, q, e=None):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.unit_size = get_unit_size(self.n)
        if e is None or euclid_alg(self.phi, e) != 1:
            self.e = get_coprime(self.phi)
        else:
            self.e = e
        _, self.d = euclide_ext_alg(self.phi, self.e)
        if self.d < 0:
            self.d += self.phi

    def decode_unit(self, unit):
        return mpow(unit, self.d, self.n)

    def decode_text(self, txt):
        data = [padd(self.decode_unit(int(x)), self.n) for x in txt.split()]
        data = unit_to_ascii(data, self.unit_size)
        return "".join([ascii_to_text(int(x)) for x in data])

    def get_public_key(self):
        return self.n, self.e



class EncoderRSA:
    def __init__(self, n, e):
        self.n = n
        self.e = e
        self.unit_size = get_unit_size(self.n)

    def encode_unit(self, unit):
        
        p = mpow(int(unit), self.e, self.n)
        return p

    def encode_text(self, txt):
        data = [padd(x) for x in text_to_ASCII(txt)]
        data = ascii_to_unit(data, self.unit_size)
        return " ".join([padd(self.encode_unit(x), self.n) for x in data])

def test():
    for p in [7793, 6269, 5683, 4441, 5153]:
        for q in [7793, 6269, 5683, 4441, 5153]:
            if p == q : continue
            d = DecoderRSA(p, q)
            e = EncoderRSA(d.n, d.e)
            s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
            et = e.encode_text(s)
            dt = d.decode_text(et)
            assert s[:50] == dt[:50]
            s = 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which dont look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isnt anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.'
            et = e.encode_text(s)
            dt = d.decode_text(et)
            assert s[:100] == dt[:100]
    print(dt)
    
    
if __name__ == '__main__':
    opcion = -1
    while opcion != 0 and opcion != 1:
        try:
            opcion = int(input('Ingrese número correspondiente\n0 - Decodificar\n1 - Codificar\n'))
        except:
            pass
        
    if opcion == 0:
        p = 0
        while p < 1:
            try:
                p = int(input('\nIngrese p\n'))
            except:
                pass
    
        q = 0
        while q < 1:
            try:
                q = int(input('\nIngrese q\n'))
            except:
                pass  
            
        e = 0 
        while e < 1:
            try:
                e = int(input('\nIngrese e\n'))
            except:
                pass 
            
        
        
        d = DecoderRSA(p, q, e)
        opcion = -1
        while opcion != 0 and opcion != 1:
            try:
                opcion = int(input('Ingrese número correspondiente\n0 - Mostrar llave\n1 - Decodificar\n'))
            except:
                pass
            
        if opcion == 0:
            print('\nLlave pública\n', d.get_public_key())
        else:
            c = input('\nIngrese mensaje encriptado\n')
            print('\nMensaje desencriptado:\n' + d.decode_text(c))
        
    else:
        n = 0
        while n < 1:
            try:
                n = int(input('\nIngrese n\n'))
            except:
                pass
    
        e = 0
        while e < 1:
            try:
                e = int(input('\nIngrese e\n'))
            except:
                pass  
        
        m = input('\nIngrese mensaje\n')
        
        e = EncoderRSA(n, e)
        
        print('\nMensaje encriptado\n' + e.encode_text(m))

