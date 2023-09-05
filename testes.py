# Arquivo de testes
"""
import numpy as np
import matplotlib.pyplot as plot

a = np.asarray([[1, 2, 3]]).T

b = np.asarray([4, 5, 6])


print(len(a))
print(a.shape)

"""
import RobPy as rp

a = rp.cria_vetor3([1, 2, 3])
b = rp.cria_vetor3([4, 5, 6])

print(rp.produto_escalar(a, b))

print(a.shape)
print(type(a))