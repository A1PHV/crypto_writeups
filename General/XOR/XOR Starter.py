from pwn import *

a = "label"
print(xor(a, 13))