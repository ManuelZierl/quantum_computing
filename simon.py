from pprint import pprint

from sympy import Matrix, sqrt
from sympy.physics.quantum import TensorProduct



Q_BITS = 4

H = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
H_n = TensorProduct(*([H] * Q_BITS))

REG_A = Matrix([1] + [0] * ((2 ** Q_BITS) - 1))  # |a> <- |0 ... 0 >
REG_B = Matrix([1] + [0] * ((2 ** Q_BITS) - 1))  # |b> <- |0 ... 0 >

REG_A = H_n * REG_A
pprint(REG_A)
print(REG_A.evalf())
pprint(REG_B)

# todo ...