from euclide_ext_alg import *

def hard_inverse(phi, e):
    for i in range(1, phi):
        if (e * i) % phi == 1:
            return i 
        
def text_to_ASCII(text):
    return [ord(x) for x in text]

def padd(ascii, n = 256):
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
        if int('256' * i) > n :
            return  i - 1
    
def ascii_to_unit(data, unit_size):
    result = []
    if len(data) % unit_size != 0 :
        data = data + ['0'* 3] * (unit_size - len(data) % unit_size)
    
    for i in range(len(data)// unit_size):
        result.append("".join(data[unit_size * i : unit_size * (i + 1)]))
    return result 

def unit_to_ascii(data, unit_size):
    result = []
    for x in data:
        x = x[unit_size - len(x) % unit_size : ]
        for i in range(len(x) // 3):
            result.append(x[3 * i : 3 * (i + 1)])
    return result

    