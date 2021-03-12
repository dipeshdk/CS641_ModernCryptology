import random

def generate_32_bit_string():
    s = ""
    for i in range(32):
        s += str(random.randint(0,1))
    return s

input_list = []

for i in range(256):
    R = generate_32_bit_string()
    L = generate_32_bit_string()
    L1 = generate_32_bit_string()
    input_list.append(L1 + R)
    input_list.append(L + R)

with open("input_binray_strings.txt", "w") as f:  
    for i in input_list:
        f.write(i + "\n")

print("input_generator.py work done")