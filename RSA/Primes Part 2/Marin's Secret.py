from Crypto.Util.number import long_to_bytes, inverse

n = "Ctrl+C/Ctrl+V from file"
e = 65537
c = "Ctrl+C/Ctrl+V from file"

z = n - 1
a = 0

while z % 2 == 0:
    z //= 2
    a += 1

p = (2 ** a - 1)
q = n // p

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

m = pow(c, d, n)

print(long_to_bytes(m))