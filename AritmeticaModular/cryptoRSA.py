'''
Manuel Alejandro Martínez Flores
Encriptación RSA
'''

from power import power_rec2 as mpow
from euclide_ext_alg import *
from util import *

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
        return "".join([chr(int(x)) for x in data])

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
    # opcion = -1
    # while opcion != 0 and opcion != 1:
    #     try:
    #         opcion = int(input('Ingrese número correspondiente\n0 - Decodificar\n1 - Codificar\n'))
    #     except:
    #         pass
        
    # if opcion == 0:
    #     p = 0
    #     while p < 1:
    #         try:
    #             p = int(input('\nIngrese p\n'))
    #         except:
    #             pass
    
    #     q = 0
    #     while q < 1:
    #         try:
    #             q = int(input('\nIngrese q\n'))
    #         except:
    #             pass  
            
    #     e = 0 
    #     while e < 1:
    #         try:
    #             e = int(input('\nIngrese e\n'))
    #         except:
    #             pass 
            
        
        
    #     d = DecoderRSA(p, q, e)
    #     opcion = -1
    #     while opcion != 0 and opcion != 1:
    #         try:
    #             opcion = int(input('Ingrese número correspondiente\n0 - Mostrar llave\n1 - Decodificar\n'))
    #         except:
    #             pass
            
    #     if opcion == 0:
    #         print('\nLlave pública\n', d.get_public_key())
    #     else:
    #         c = input('\nIngrese mensaje encriptado\n')
    #         print('\nMensaje desencriptado:\n' + d.decode_text(c))
        
    # else:
    #     n = 0
    #     while n < 1:
    #         try:
    #             n = int(input('\nIngrese n\n'))
    #         except:
    #             pass
    
    #     e = 0
    #     while e < 1:
    #         try:
    #             e = int(input('\nIngrese e\n'))
    #         except:
    #             pass  
        
    #     m = input('\nIngrese mensaje\n')
        
    #     e = EncoderRSA(n, e)
        
    #     print('\nMensaje encriptado\n' + e.encode_text(m))
    
    
    test()








