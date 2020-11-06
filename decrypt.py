import pyAesCrypt, os
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
file=input("File:")
password = input("Password:")
# encrypt
pyAesCrypt.decryptFile(file, file[:-4], password, bufferSize)
os.system("rm "+file)
