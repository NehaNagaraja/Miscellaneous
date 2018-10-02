import sys              #to read the command-line arguments
import subprocess       #to run another python script
import re               #for matching regular expressions
from fractions import gcd as bltin_gcd          #to find the GCD of 2 numbers

class RSA:
    def __init__(self,e):
        self.e = e

    def select_p_q(self):
        self.p = subprocess.check_output([sys.executable, "PrimeGenerator.py"])     # subprocess to generate p for encryption
        self.p = int(re.search(r'\d+', self.p).group())                             # get the prime number from the string
        self.q = subprocess.check_output([sys.executable, "PrimeGenerator.py"])     # subprocess to generate p for encryption
        self.q = int(re.search(r'\d+', self.q).group())                             # get the prime number from the string
        self.n = self.p * self.q                                                    # find n = p*q
        print "p = ", self.p
        print "q = ", self.q
        print "n = ", self.n
        print "Public key, e = ", self.e
        self.phi = (self.p - 1) * (self.q - 1)                   # find phi = (p-1) * (q-1)
        #print phi
        if self.p == self.q:                                     # if p and q generated are equal
            rsa1 = self.select_p_q()                             # generate p and q again
        if (bltin_gcd(self.phi, self.e) == 1) == False:          # if phi and e are not co - prime
            rsa1 = self.select_p_q()                             # generate p and q again

    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def modinv(self,a,m):
        g, x, y = self.egcd(a, m)
        return x % m

    def encrypt(self,source_file,destn_file):       # function to encrypt the file
        file_rd = open(source_file, 'rw')           # open the file to be encrypted in read write mode
        message = file_rd.read()                    # read the contents of the file
        ln = len(message.encode('utf-8'))           # count the number of bits in the file
        if ln == 128:                               # if number of bits in the source file = 128
            ad = ("0" * 128)
            message = ad + message                  # prepend 128 0's to the file contents
        elif ln%128 != 0:                           # if number of bits in the source file is not a multiple of 128
            rem = ln % 128
            ad = ("\n" * (128-rem))
            message = message + ad                  # append new line characters to the file contents to get multiple of 128
        ciphertext = [(ord(char) ** e) % self.n for char in message]
        enc_text = (' '.join(map(lambda x: str(x), ciphertext)))            #encrypt the file contents
        file_write = open(destn_file,'w+')          # open the file in write mode, create a new file if not present
        file_write.write(str(self.p))               # write 'n' to the file to be used for decryption
        file_write.write(" ")
        file_write.write(str(self.q))             # write 'phi' to the file to be used to find the private key
        file_write.write(" ")
        file_write.write(enc_text)             # write encrypted data to the file to be decrypted
        print "Encryption successful!"

    def decrypt(self,source_file,destn_file):
        file_rd = open(source_file, 'rw')           # open the file to be decrypted in read write mode
        message = file_rd.read()                    # read the contents of the file
        #print message
        lst1 = map(int, message.split())            # split to get the values as a list
        p = lst1[0]
        q = lst1[1]
        phi = (p-1) * (q-1)
        d = self.modinv(self.e,phi)                 # to find the private key for the combination
        dp = pow(d, 1, p - 1)
        #print "dp =", dp
        dq = pow(d, 1, q - 1)
        #print "dq =", dq
        #print "message = ", message
        msg = ''
        for ch in range(2,len(lst1)):
            l = lst1[ch]
            m1 = pow(l,dp,p)
            #print "m1 = ", m1
            m2 = pow(l, dq, q)
            #print "m2 = ", m2
            qinv = self.modinv(q,p)
            #print "qinv =", qinv
            val = (qinv * (m1-m2)) % p
            #print "val = ", val
            mg = m2 + val * q
            #print "msg =", mg
            msg += chr(mg)
        #return msg[self.rem:]
        file_write1 = open(destn_file, 'w+')
        rem =  msg.find('\n')
        print rem
        print msg[:rem]
        file_write1.write(msg[:rem])
        print "Decryption successful!"


if __name__ == '__main__':
    e = 65537                           #public key e set as in the problem
    rsa1 = RSA(e)                       #creating an object of the RSA class to access the attributes and functions
    source_file = sys.argv[3]           #getting the source file for the operation to be performed
    destn_file = sys.argv[4]            #getting the source file for the operation to be performed
    if 'e' in sys.argv[2]:              #if user wants to encrypt - '-e' in the arguments
        rsa1.select_p_q()               #to generate p and q values for encryption
        enc_text = rsa1.encrypt(source_file,destn_file)         #to encrypt the file
    elif 'd' in sys.argv[2]:            #if user wants to encrypt - '-e' in the arguments
        rsa1.decrypt(source_file,destn_file)






