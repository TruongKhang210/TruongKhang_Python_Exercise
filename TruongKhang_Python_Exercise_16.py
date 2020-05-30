# https://dev.to/spaceofmiah/generating-random-password-in-python-practical-guide-amd

import string
import random


def passlength():
    len = input("how strong do you want your password (weak , strong ) : ")
    if len == 'strong' :
        len = int(input("how long do you want your password : "))
        return len
    elif len == 'weak':
        len = random.randint(1, 3)
        return len


def passgen(len=8):
    so = string.digits
    # chu = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    # 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chu = string.ascii_letters
    # help(string) ham giai thich
    kt = string.punctuation
    printable = so + chu + kt  # printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    '''F-strings provide a way to embed expressions inside string literals, using a minimal syntax.
It should be noted that an f-string is really an expression evaluated at run time, not a constant value.
In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside braces'''
    printable = list(printable)
    random.shuffle(printable)
    randpass = random.choices(printable, k=len)
    randpass = ''.join(randpass)
    return randpass



if __name__ == '__main__':
    len1 = passlength()
    pass1 = passgen(len1)
    print("your random password : " + pass1)




