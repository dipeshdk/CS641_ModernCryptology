import utils

# this matrix will be changed after we find the matrix from the input output pairs 
MATRIX_A = [[84, 114, 20, 127, 98, 31, 15, 90], [0, 70, 17, 20, 37, 51, 121, 14], [0, 0, 43, 26, 3, 28, 14, 81], [0, 0, 0, 12, 104, 32, 104, 25], [0, 0, 0, 0, 112, 100, 0, 10], [0, 0, 0, 0, 0, 11, 92, 68], [0, 0, 0, 0, 0, 0, 27, 31], [0, 0, 0, 0, 0, 0, 0, 38]]

MATRIX_EXP = [20, 108, 37, 78, 88, 50, 23, 17]
def decrypt_password(password):
    password_in_byte = utils.block_to_byte(password)
    op = ""
    
    for i in range(0,8):
        for j in range(0,128):
            input = op  + utils.byte_to_char(j) + (14-len(op))*'f'
            
            if ord(password_in_byte[i]) == utils.eaeae(utils.block_to_byte(input), MATRIX_A, MATRIX_EXP)[i]:
                op += utils.byte_to_char(j)
                break
    
    return op


password_first_half = "lhmiflkkhnimfqkl"
password_second_half = "kfhohmgllukpjjfj"

pass_first_half_decrypted = utils.block_to_byte(decrypt_password(password_first_half))
pass_second_half_decrypted = utils.block_to_byte(decrypt_password(password_second_half))

print(pass_first_half_decrypted + pass_second_half_decrypted)