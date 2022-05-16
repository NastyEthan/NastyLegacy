import hashlib # there could be a better hashing function, but this works

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
white = "\033[37m"

def check(a,b):
    if a == b:
        print(green + 'SUCCESS!!!' + white) # :D
    else:
        print(red + "FAILURE" + white) # failure of course

# password encrypting
password = hashlib.sha512(b'CyberS2cUr!tY').hexdigest()
print(yellow + "SHA512 hash of password" + white)
print(password)

# user input
userinput = input(yellow + "what's the password: " + white)
encrypted = hashlib.sha512(userinput.encode()).hexdigest()
print(yellow + "SHA512 hash of input" + white)
print(encrypted) # checking x2)

# function call
check(password,encrypted)