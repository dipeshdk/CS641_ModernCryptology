import numpy as np
import random
import sympy as sp
from numpy.linalg import matrix_rank
np.set_printoptions(threshold=np.inf)
from pyfinite import ffield
import req_functions as rf 

def eaeae (plaintext, linearMatrix, exponentMatrix):
    plaintext = [ord(c) for c in plaintext]
    ciphertext0 = [0]*8
    for i, c in enumerate(plaintext):
        ciphertext0[i] = rf.Exponential(c, exponentMatrix[i])

    ciphertext1 = rf.linear_transformation(linearMatrix, ciphertext0)

    ciphertext2 = [0]*8
    for i, c in enumerate(ciphertext1):
        ciphertext2[i] = rf.Exponential(c, exponentMatrix[i])

    ciphertext3 = rf.linear_transformation(linearMatrix, ciphertext2)
    ciphertext4 = [0]*8
    for i, c in enumerate(ciphertext3):
        ciphertext4[i] = rf.Exponential(c, exponentMatrix[i])
    return ciphertext4