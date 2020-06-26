from random import *
from string import *

def passwordGen(m2, m1):
    spec = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    a = []
    b = []
    c = []
    d = []
    for i in range(randint(m2, m1) // 4 or 2):
        a.append(str(randint(0, 9)))
    for i in range(randint(m2, m1) // 4 or 2):
        b.append(choice(ascii_uppercase))
    for i in range(randint(m2, m1) // 4 or 2):
        c.append(choice(ascii_lowercase))
    for i in range(randint(m2, m1) // 4 or 2):
        d.append(choice(spec))
    return (a+b+c+d)

m1 = int(input("Enter maximum length of password : "))
m2 = int(input("Enter minimum length of password : "))
if m2<6:
    g = passwordGen(6, m1)
else:
    g = passwordGen(m2,m1)
g = ''.join(g)
print("Recommended password :", end=" ")
print(g)
