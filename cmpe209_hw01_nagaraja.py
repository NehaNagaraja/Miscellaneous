import sys
from Crypto.Cipher import AES #importing library required for AES encryption
from Crypto import Random #importing library to generate a random Initialization vector for the encryption and decryption

def encrypt(key,iv):
    inputfile = 'plaintext.txt'
    outputfile = 'encryptedtext.txt'
    file_read = open(inputfile, 'rwb')  # opening the text file to be encrypted in read mode
    data = file_read.read()  # reading the contents to be encrypted
    cipher = AES.new(key, AES.MODE_CFB, iv)  # creates a new AES cipher
    msg = cipher.encrypt(data).encode('hex')  # encypts the data using the cipher created in hex format
    file_read = open(outputfile, 'w')  # opening the text file to write the encrypted data in write mode
    file_read.write(msg)  # writing the encrypted data to encryptedtext.txt
    print "Encryption complete"

def decrypt(key,iv):
    inputfile = 'encryptedtext.txt'
    outputfile = 'decryptedtext.txt'
    file_read = open(inputfile, 'rwb')  # opening the text file to be encrypted in read mode
    encdata = file_read.read()  # reading the contents to be encrypted
    enc = encdata.decode('hex')  # decode the data saved in hex to decrypt
    aes = AES.new(key, AES.MODE_CFB, iv)  # creates a new AES cipher
    msg1 = aes.decrypt(enc)  # encypts the data using the cipher created
    file_read = open(outputfile, 'w')  # opening the text file to wroutputfileite the decrypted data in write mode
    file_read.write(msg1)  # writing the decrypted data to decryptedtext.txt
    print "Decryption complete"

def main():
    key = 'lukeimyourfather'  # 16-bit key to be used for encryption
    iv = Random.new().read(AES.block_size)  # Initialization vector generated for the encryption and decryption process

    encrypt(key,iv)
    decrypt(key,iv)

if __name__ == "__main__":
    main()