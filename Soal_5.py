from hashlib import sha256
from time import time

def hash(s):
    return sha256(s.encode('ascii')).hexdigest()

def cetak(n):
    random_string=[hash(str(time()))[:32]]
    for i in range(n):
        random_string.append(hash(random_string[i])[:32])
        print(random_string[i])
    for i in range(n):
        for j in range(i):
            if random_string[i]==random_string[j]:
                raise Exception('Ada dua string yang sama!')
