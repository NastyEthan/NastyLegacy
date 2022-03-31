from cryptography.fernet import Fernet
import rsa

passwords = []


def symmKey():
    global passwords
    password = str(input("password to encrypt: "))

    key = Fernet.generate_key()
    fernet = Fernet(key)

    encryptedPassword = fernet.encrypt(password.encode())

    print("original password: ", password)
    print("encrypted password: ", encryptedPassword)

    decryptedPassword = fernet.decrypt(encryptedPassword).decode()

    print("decrypted password: ", decryptedPassword)

    info = [password, encryptedPassword, key]
    passwords.append(info)


def asymmKey():
    # Two keys, since its asymmetric encryption
    publicKey, privateKey = rsa.newkeys(512)

    message = str(input("message to encrypt: "))

    encMessage = rsa.encrypt(message.encode(), publicKey)

    print("original string: ", message)
    print("encrypted string: ", encMessage)

    decMessage = rsa.decrypt(encMessage, privateKey).decode()
    print("decrypted string: ", decMessage)


def tester():
    global passwords
    choose = input("symm or asymm ")
    try:
        if choose == "symm":
            symmKey()
        elif choose == "asymm":
            asymmKey()
    except:
        print("try again")
    print(passwords)

if __name__ == "__main__":
    tester()