import random

def generate_32_bit_string():
    s = ""
    for i in range(32):
        s += str(random.randint(0,1))
    return s


def to_char(s):
    to_letter = {"0000": "f", "0001": "g", "0010": "h", "0011": "i", "0100": "j", "0101": "k","0110":"l", "0111":"m","1000": "n","1001": "o", "1010": "p","1011":"q","1100":"r","1101":"s","1110":"t","1111": "u"}
    i = 0
    t = ""

    while i < 64:
        tmp = s[i:i+4]
        t += to_letter[tmp]
        i += 4

    return t


def IP_inv(s):
    IP_inverse = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

    t = ""

    for i in range(64):
        t += s[IP_inverse[i]-1]

    return t


input_list = []

for i in range(256):
    R = generate_32_bit_string()
    L = generate_32_bit_string()
    L1 = generate_32_bit_string()
    input_list.append(L1 + R)
    input_list.append(L + R)

# Uncomment this portion of code if you want to see input in binary strings
# with open("input_binray_strings.txt", "w") as f:  
#     for i in input_list:
#         f.write(i + "\n")

actual_plain_text = []

for i in input_list:
    pt_bits = i
    pt_char = to_char(pt_bits)
    actual_plain_text.append(pt_char)

with open("input_plain_text.txt", "w") as f:
    for i in actual_plain_text:
        f.write(i + "\n")

print("input_generator.py work done")