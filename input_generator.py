import random

def generate_64_bit_string():
    s = ""
    for i in range(64):
        s += str(random.randint(0,1))
    return s


def to_char(s):
    to_letter = {"0000": "f",
                 "0001": "g",
                 "0010": "h",
                 "0011": "i",
                 "0100": "j",
                 "0101": "k",
                 "0110": "l",
                 "0111": "m",
                 "1000": "n",
                 "1001": "o",
                 "1010": "p",
                 "1011": "q",
                 "1100": "r",
                 "1101": "s",
                 "1110": "t",
                 "1111": "u"}
    i = 0
    t = ""

    while i < 64:
        tmp = s[i:i+4]
        t += to_letter[tmp]
        i += 4

    return t


def IP_inv(s):
    IP_inverse = [  40, 8, 48, 16, 56, 24, 64, 32,
                    39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30,
                    37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28,
                    35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26,
                    33, 1, 41,  9, 49, 17, 57, 25]

    t = ""

    for i in range(64):
        t += s[IP_inverse[i]-1]

    return t


def send_to_file(input_list, filename):
    actual_plain_text = []

    for i in input_list:
        pt_bits = i
        pt_bits = IP_inv(pt_bits)
        pt_char = to_char(pt_bits)
        actual_plain_text.append(pt_char)

    with open(filename, "w") as f:
        for i in actual_plain_text:
            f.write(i + "\n")


input_list1 = []
input_list2 = []

psi1 = 0x4008000004000000
psi2 = 0x0020000800000400

for i in range(5000):
    s = generate_64_bit_string()
    
    p1 = int(s,2)
    p2 = p1 ^ psi1
    p3 = p1 ^ psi2
    p4 = p2 ^ psi2
    
    b1  = '{:064b}'.format(p1)
    b2  = '{:064b}'.format(p2)
    b3  = '{:064b}'.format(p3)
    b4  = '{:064b}'.format(p4)

    # for characteristic equation 1
    input_list1.append(b1)
    input_list1.append(b2)
    
    input_list1.append(b3)
    input_list1.append(b4)

    # for characteristic equation 2
    input_list2.append(b1)
    input_list2.append(b3)
    
    input_list2.append(b2)
    input_list2.append(b4)


# Uncomment this portion of code if you want to see input in binary stringsfilename = "input_plain_text.txt"
# with open("input_binray_strings.txt", "w") as f:  
#     for i in input_list:
#         f.write(i + "\n")

send_to_file(input_list1, "input_plain_text_9.txt")
send_to_file(input_list2, "input_plain_text_10.txt")

print("input_generator.py work done")