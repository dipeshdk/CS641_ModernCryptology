# name will be changed to utils.py afterwords
from pyfinite import ffield

binToCharDict = {'0000': 'f',
                '0001': 'g',
                '0010': 'h',
                '0011': 'i',
                '0100': 'j',
                '0101': 'k',
                '0110': 'l',
                '0111': 'm',
                '1000': 'n',
                '1001': 'o',
                '1010': 'p',
                '1011': 'q',
                '1100': 'r',
                '1101': 's',
                '1110': 't',
                '1111': 'u'}


def byte_to_char(byte):    
    binnum = '{:08b}'.format(byte)
    c1 = binToCharDict[binnum[0:4]]
    c2 = binToCharDict[binnum[4:8]]
    return c1 + c2


def block_to_byte(c):
    plainText = ""
    for i in range(0, len(c), 2):
        plainText += chr( ord(c[i+1]) - ord('f') + 16*(ord(c[i]) - ord('f')))
    
    return plainText


def add_num (n1, n2):
    return int(n1) ^ int(n2)


F = ffield.FField(7)
def multiply_num (n1, n2):
    return F.Multiply(n1, n2)


def add_two_vectors (vector1, vector2):
    ans = []
    
    for element1, element2 in zip(vector1, vector2):
        ans.append(add_num(element1, element2))
    
    return ans


def multiply_scalar_to_vector (vector, scalar):
    ans = []
    
    for element in vector:
        ans.append(multiply_num(element, scalar))
    
    return ans


def linear_transformation (matrix, elist):
    ans = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for row, elem in zip(matrix, elist):
        temp = multiply_scalar_to_vector(row, elem)
        ans = add_two_vectors(temp, ans)
    
    return ans


store_exp = []
for i in range(128):
    store_exp.append([-1]*128)


def Exponential(num, power):
    if store_exp[num][power] != -1:
        return store_exp[num][power]

    
    if power == 0:
        store_exp[num][power] = 1
        return store_exp[num][power]
    
    if power == 1:
        store_exp[num][power] = num
        return store_exp[num][power]
    
    
    if power%2 == 0:
        sqrt_no = Exponential(num, power>>1)
        store_exp[num][power] = multiply_num(sqrt_no, sqrt_no)
        return store_exp[num][power]
    else:
        sqrt_no = Exponential(num, power>>1)
        temp = multiply_num(sqrt_no, sqrt_no)
        store_exp[num][power] = multiply_num(num, temp)
        return store_exp[num][power]