from random import randint

from mpmath import expm
from numpy.random import choice
import numpy as np
from sympy import Matrix, init_printing, sqrt, pprint, Matrix
from sympy.physics.quantum import TensorProduct


def measure(S):
    prob = [x ** 2 for x in S]
    draw = choice(list(range(0, len(S))), 1, p=prob)[0]
    m = [0] * len(S)
    m[draw] = 1
    S = Matrix([m])
    return S


Q_BITS = 5

# ORACLE = Matrix([[0] * (2 ** Q_BITS)])
R = randint(0, (2 ** Q_BITS)) - 1
a = np.identity(2 ** Q_BITS, dtype=int)
a[R][R] = -1
ORACLE = Matrix(a)

H = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
H_n = TensorProduct(*([H] * Q_BITS))
R_n = Matrix(np.identity(2 ** Q_BITS, dtype=int))
R_n[0] = -1
D_n = -H_n * R_n * H_n
STATE = Matrix([1] + [0] * ((2 ** Q_BITS) - 1))  # )

STATE = H_n * STATE

# use the oracle -> STATE = ORACLE * STATE
# use the mirror on average -> STATE = D_n * STATE
