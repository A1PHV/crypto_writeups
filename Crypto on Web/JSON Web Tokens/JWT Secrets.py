import jwt
encoded = jwt.encode({'username':'cb','admin':'true'},'secret',algorithm='HS256')
print(encoded)