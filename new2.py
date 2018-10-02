from collections import OrderedDict
d={}
d['A'] = 3
d['R'] = 1
d['c'] = 4

e=65537
n = 99869571083949871712789729314404395977114991159184681207722221468057958565079

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c


s = "The time has come to talk of many things: of shoes and ships and sealing-wax of cabbages and kings and why the sea is boilin000g"
print len(s.encode('utf-8'))
print (ord(x) for x in list(s))
for i in list(s):
    print chr(ord(i))
#print ''.join([chr(encrypt_block(ord(x))) for x in list(s)])