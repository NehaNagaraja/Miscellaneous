import os, random, struct
import binascii
from Crypto.Cipher import AES
from Crypto import Random

# The key used for AES encrption and decryption
key = "lukeimyourfather"
#Initialization
IV = Random.new().read(AES.block_size)

#Input file
filename1 = "plaintext.txt"
filename2 = "encryptedtext.txt"
filename3 = "decryptedtext.txt"

# Reaading from the input file
with open(filename1, "rb") as fileread:
    read_line = fileread.read()

#Encryption
cipher = AES.new(key, AES.MODE_CFB, IV)
data = cipher.encrypt(read_line)

#Output file
out_file = open (filename2, "w")

data1 = data.encode('hex')

# #Converting to hex bytes
# data1 = binascii.hexlify(data)

# #Converting to hex string
# data2 = data1.decode()

# Encrypted data is written in hex format to file "encryptedtext.txt"
out_file.write(data1)
fileread.close()
out_file.close()

with open(filename2, "r") as fileread1:
    read_line1 = fileread1.read()

data4 = read_line1.decode('hex')

out_file1 = open (filename3, "w")
cipher1 = AES.new(key, AES.MODE_CFB, IV)

data_decrypt = cipher1.decrypt(data4)
data3 = str (data_decrypt)
print (data_decrypt)
print (data3)

out_file1.write(data3)