print('Kartik')

a = 2*2
print(a, type(a))

b =3+5
print(b, type(b))

c = 'chai'*4
print(c,type(c))

# print(tear)
# NameError: name 'tear' is not defined

# module
import os
print(os.getcwd())
print(os.mkdir("kart")) #return None
print(os.removedirs("kart"))  #return None
for c in "Kartik":
    print(c)

import sys
print(sys.platform)

from ch01_First.First import chai
chai("FG")