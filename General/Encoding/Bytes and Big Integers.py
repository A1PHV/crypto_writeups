from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

# given an encoding and the data, it decodes it.
def decode(encoding, data):
    if encoding == "base64":
        decoded = base64.b64decode(data).decode('ascii')
    elif encoding == "hex":
        bytes_object = bytes.fromhex(data)
        decoded = bytes_object.decode("ASCII")
    elif encoding == "rot13":
        decoded = codecs.decode(data, 'rot_13')
    elif encoding == "bigint":
        decoded = long_to_bytes(int(data, 16)).decode('ascii')
    elif encoding == "utf-8":
        decoded = "".join([chr(b) for b in data])
    return decoded

for i in range(0, 100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    ## add decoded thing here and send that back
    decoded = decode(received["type"], received["encoded"])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

received = json_recv()
print(received)