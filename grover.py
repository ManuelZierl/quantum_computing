from random import randint
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


Q_BITS = 2

#_ORACLE = Matrix([[0] * (2 ** Q_BITS)])
a = np.identity(2 ** Q_BITS, dtype=int)
r = randint(0, (2 ** Q_BITS)) - 1
a[r][r] *= -1
_ORACLE = Matrix(a)
#_ORACLE[randint(0, (2 ** Q_BITS)) - 1] = 1  # THE ORACEL GIVE 0 FOR ALL EXECPT OF ONE STATES
#_ORACLE[randint(0, (2 ** Q_BITS)) - 1] = 1  # THE ORACEL GIVE 0 FOR ALL EXECPT OF ONE STATES
pprint(_ORACLE)

H = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
H_n = TensorProduct(*([H] * Q_BITS))
R_n = Matrix(np.identity(2 ** Q_BITS, dtype=int))
R_n[0] = -1
D_n = -H_n * R_n * H_n
STATE = Matrix([1] + [0] * ((2 ** Q_BITS) - 1))  # )
H_BIT = Matrix([0] + [1])

H_BIT = H * H_BIT
STATE = H_n * STATE

#pprint(((-1) ** ((_ORACLE * STATE)[0]))*H_BIT)


# STATE = (1 ** ((_ORACLE * STATE)[0]) * _ORACLE)*D_n <-- ??

STATE = STATE * ((-1) ** ((_ORACLE * STATE)[0]))

#pprint(STATE)

"""


pprint(_ORACLE)
pprint(STATE)

pprint(_ORACLE * STATE)
pprint(STATE * _ORACLE)


pprint(((-1) ** ((STATE*_ORACLE)[0])) * STATE)
pprint(STATE * _ORACLE * STATE)
pprint(D_n * STATE)


# pprint(STATE*((-1) ** ((_ORACLE * STATE))))
pprint(_ORACLE)
print("-------")
pprint(STATE)

# H_BIT = ((-1) ** ((_ORACLE * STATE)[0])) * H_BIT






#



#print((STATE*_ORACLE)[0])
#print((-1)**((STATE*_ORACLE)[0]))
#print(-1**(1/2))
#print(pow((-1),((STATE*_ORACLE)[0])))



pprint(STATE)

pprint(STATE)

pprint("OBQACHT")

pprint(STATE)
pprint(_ORACLE)
pprint(STATE*_ORACLE)

#STATE = D_n*STATE*_ORACLE
#pprint(STATE)
#STATE = STATE*D_n#*((-1**(STATE*_ORACLE)[0])*_ORACLE)# *(-1**(STATE*_ORACLE)[0])
#STATE = D_n *((-1**(STATE*_ORACLE)[0])*STATE)# *(-1**(STATE*_ORACLE)[0])
#pprint(STATE)

#r = Matrix([[1/2,1/2,-1/2,1/2]])
#pprint(r)
#pprint(-H_n*R_n*H_n*())



#STATE = measure(STATE)





#pprint(STATE*TensorProduct(H, H))


#print(M*Matrix([1,0,0,0]))
#"""
