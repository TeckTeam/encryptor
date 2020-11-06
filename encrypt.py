import pyAesCrypt
import os
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
file = input("File:")
password = input("Password:")
# encrypt
pyAesCrypt.encryptFile(file, file+".aes", password, bufferSize)
os.system("rm "+file)
