# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
import requests


alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
base = len(alphabet)

counter = 0
length = 0

while True:
    #counter -> str at base -> password
    password = ''
    number = counter
    while number > 0:
        # counter = x * base + rest
        x = number // base
        rest = number % base
        password = alphabet[rest] + password
        number = x
    while len(password) < length:
        password = alphabet[0] + password
    #check password
    print(length, counter, password)

    response = requests.get('http://127.0.0.1:5000/auth',
                            json = {'login':'cat', 'password': password})

    if response.status_code == 200:
        print('SUCCESS', password)
        break

    if alphabet[-1] * length == password:
        length += 1
        counter = 0
    else:
        counter += 1