#a program that generate random password
import random
import string
chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits='0123456789'
punc='!@#$%^&*()_+'
def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(chars + digits + punc)
    return password
if __name__ == "__main__":
    length = int(input("Enter length of password: "))
    print("Password: ", generate_password(length))
    
    