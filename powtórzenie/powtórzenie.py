def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    else:
        return a

def nww(a, b):
    x = a * b
    wynik = int(x / nwd(a, b))
    return wynik

def rozkład(n):
    czynniki = []
    k = 2
    if n == 1 or n == 2:
        czynniki.append(n)
    else:
        while n != 1:
            if n % k == 0:
                n = n // k
                czynniki.append(k)
            else:
                k += 1
    return czynniki

def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    prime = int(n ** 0.5) + 1
    for dzielniki in range(3, prime, 2):
        if n % dzielniki == 0:
            return False
    return True

def silnia(n):
    wynik = 1
    list = []
    for i in range(n):
        list.append(i + 1)
    for i in list:
        wynik *= i
    return wynik

import string
alfabet = string.ascii_lowercase

def cezar(file, key):
    for line in file:
        wynik = ''
        line = line.strip()
        for i in line:
            if i == ' ':
                wynik += ' '
            else:
                wynik += alfabet[(alfabet.index(i) + 1) % len(alfabet)]
        filew.write(wynik + '\n')


file = open('dane', 'r')
filew = open('odpowiedzi', 'w')

print('nwd', nwd(10, 5))
print('nww', nww(5, 10))
print('rozkład', rozkład(24))
print('isprime', isprime(13))
print('silnia', silnia(4))
print('cezar', cezar(file, 1))

file.close()
filew.close()
