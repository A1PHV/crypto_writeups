from Crypto.Util.number import *
print((2*11*17*inverse(11*17,5) + 3*5*17*inverse(5*17,11) + 5*5*11*inverse(5*11,17)) % 935)