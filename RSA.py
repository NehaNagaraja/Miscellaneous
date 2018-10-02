import sys              #to read the command-line arguments
import subprocess       #to run another python script
import re               #for matching regular expressions
from fractions import gcd as bltin_gcd
#import BitVector
#import gmpy

class RSA:
    def __init__(self,e):
        self.e = e

    def select_p_q(self):
        self.p = subprocess.check_output([sys.executable, "PrimeGenerator.py"])
        self.p = int(re.search(r'\d+', self.p).group())
        self.q = subprocess.check_output([sys.executable, "PrimeGenerator.py"])
        self.q = int(re.search(r'\d+', self.q).group())
        self.n = self.p * self.q
        print "p = ", self.p
        print "q = ", self.q
        print "n = ", self.n
        print "Public key, e = ", self.e
        self.phi = (self.p - 1) * (self.q - 1)
        #print phi
        if self.p == self.q:
            rsa1 = self.select_p_q()
        if (bltin_gcd(self.phi, self.e) == 1) == False:
            rsa1 = self.select_p_q()

    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def modinv(self,a,m):
        g, x, y = self.egcd(a, m)
        return x % m

    def encrypt(self,source_file,destn_file):
        file_rd = open(source_file, 'rw')
        message = file_rd.read()
        ln = len(message.encode('utf-8'))
        if ln == 128:
            ad = ("0" * 128)
            message = ad + message
        elif ln%128 != 0:
            rem = ln % 128
            print rem
            ad = ("\n" * (128-rem))
            message = message + ad
        #self.rem = 256 - ln
        #ad = ("0" * (self.rem))
        #message = ad+message
        print "message= ", message
        print len(message.encode('utf-8'))
        #print len(message.encode('utf-8'))
        #print [ord(char) for char in message]
        self.ciphertext = [(ord(char) ** e) % self.n for char in message]
        #print self.ciphertext
        self.enc_text = (' '.join(map(lambda x: str(x), self.ciphertext)))
        print self.enc_text
        #return self.ciphertext
        file_write = open(destn_file,'w+')
        file_write.write(self.enc_text)
        print "Encryption successful!"
        print self.enc_text
        return self.enc_text

    def decrypt(self,d,enctext):
        dp = pow(d,1,self.p-1)
        dq = pow(d,1,self.q-1)
        #print "enctext= ", self.enc_text
        lst1 = map(int, self.enc_text.split())
        msg = ''
        for ch in lst1:
            #print ch
            m1 = pow(ch,dp,self.p)
            m2 = pow(ch, dq, self.q)
            qinv = self.modinv(self.q,self.p)
            val = (qinv * (m1-m2)) % self.p
            mg = m2 + val * self.q
            msg += chr(mg)
        #return msg[self.rem:]
        file_write1 = open(destn_file, 'w+')
        print msg[self.rem:]
        file_write1.write(msg[self.rem:])
        print "Decryption successful!"


if __name__ == '__main__':
    e = 65537
    rsa1 = RSA(e)
    rsa1.select_p_q()
    source_file = sys.argv[2]
    destn_file = sys.argv[3]
    d = rsa1.modinv(e,rsa1.phi)
    print "Private key, d =" ,d

    enc_text = rsa1.encrypt(source_file,destn_file)
    rsa1.decrypt(d,enc_text)






