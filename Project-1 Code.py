import hashlib
object = input("Enter a string to hash:")
data = hashlib.md5(object.encode())
print("MD5 hashed output is:",data.hexdigest())
