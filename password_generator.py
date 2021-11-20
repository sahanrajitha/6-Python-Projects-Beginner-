import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX!@#$%^&*().,?0123456789'

number = int(input("How many passwords do want Genarate: "))
length = int(input('Input Your password length: '))

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
