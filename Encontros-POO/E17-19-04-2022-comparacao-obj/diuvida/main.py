from one_underscore import *

ex1 = One()
print(ex1._private_attr)

# _private_function()

# ---

# Usar __ em herança (evitar conflito entre os atributos das classes)
from two_underscores import *

d2 = TwoChild()
print(d2.__private_attr)
# print(dir(d2))
