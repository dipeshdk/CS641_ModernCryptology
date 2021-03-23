import req_functions as utils
import eaeae 

# this matrix will be changed after we find the matrix from the input output pairs 
MATRIX_A = [[126, 32, 68, 126, 74, 76, 58, 39], 
            [0, 85, 100, 91, 83, 99, 111, 122], 
            [0, 0, 4, 29, 122, 69, 40, 108], 
            [0, 0, 0, 20, 17, 0, 93, 68], 
            [0, 0, 0, 0, 78, 94, 114, 78], 
            [0, 0, 0, 0, 0, 85, 77, 2], 
            [0, 0, 0, 0, 0, 0, 53, 62], 
            [0, 0, 0, 0, 0, 0, 0, 50]]

MATRIX_EXP = [88, 34, 20, 43, 26, 63, 102, 23]


def decrypt_password(password):
    password_in_byte = utils.block_to_byte(password)
    op = ""
    
    for i in range(0,8):
        for j in range(0,128):
            input = op  + utils.byte_str(j) + (14-len(op))*'f'
            
            if ord(password_in_byte[i]) == eaeae.EAEAE(utils.block_to_byte(input), MATRIX_A, MATRIX_EXP)[i]:
                op += utils.byte_str(j)
                break
    
    return op


password_first_half = "lhmiflkkhnimfqkl"
password_second_half = "kfhohmgllukpjjfj"

pass_first_half_decrypted = utils.block_to_byte(decrypt_password(password_first_half))
pass_second_half_decrypted = utils.block_to_byte(decrypt_password(password_second_half))

print(pass_first_half_decrypted + pass_second_half_decrypted)