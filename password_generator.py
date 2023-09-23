import random

print("Welcome to Your Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&?0123456789'

number = int(input("Amount of passwords to generate: "))
length = int(input("Input your password length: "))

print("\nhere are your passwords: ")

for i in range(number):
    passwords = ""
    for j in range(length):
        passwords += random.choice(chars)
    print(passwords)
    