import hashlib

result = str(input('Enter the string you would like to be converted to MD5 hash: '))
result = hashlib.md5(result.encode())

print("The hash equivalent of this string would be: ", end='')
print(result.hexdigest())