# TEST FILE

import hashlib # there could be a better hashing function, but this works

password = hashlib.sha512(b'Y0Uc@nTg3tTH!S0ne').hexdigest()
print(password) # checking

userinput = input("what's the pass: ")
encrypted = hashlib.sha512(userinput.encode()).hexdigest()
print(encrypted) # checking x2

if password == encrypted:
    print('SUCCESS!!!') # :D
else:
    print("BEANS") # beans