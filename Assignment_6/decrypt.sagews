︠b6a71905-19c4-4391-b0f3-50f340e61a3d︠
import binascii

# This function solves for the small roots of polynomial
def solve(padding, e, c, n):
#     print("popo")
    ZmodN = Zmod(n) # mod n field
    e = ZmodN(e)
    c = ZmodN(c)
    p = ZmodN(padding)
    P.<x> = PolynomialRing(ZmodN)
    f_x = (p + x)^e - c
    f_x = f_x.monic()
    x0 = f_x.small_roots() # small roots of f_x
    return x0
#     return [0]

# Given RSA values
e = 5
c = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693
n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093


# Iterating over possible length of password: 0 bytes to 25 bytes
def break_RSA(p,lol):
    for x0_length in range(0, 25):
        res = bytes(p, 'utf-8')
        p_hex = binascii.hexlify(res)
        p_int = int(p_hex, 16)
        roots = solve(p_int, e, c, n)
        if(len(roots) != 0):
            print("here")
            break # We have found the password
        else:
    #         print("lol")
            p = p + '\x00' # Left shifting the padding by 1 byte
#             print(p)
    if len(roots) != 0:
        print(len(roots))
        ans = Integer(roots[0])
        ans_hex = hex(ans)
        print(binascii.unhexlify(ans_hex))
    else:
        print("Not found")

def try_poss_edits(curr):
    break_RSA(curr, 300)  
    temp = curr + ":"
    break_RSA(temp, 300)  
    temp = curr + ": "
    break_RSA(temp, 300)  
    temp = curr + " "
    break_RSA(temp, 300)  
    temp = curr + " :"
    break_RSA(temp, 300)  
    temp = curr + " : "
    break_RSA(temp, 300)  

# Padding
poss_paddings = [0]*5
poss_paddings[0] = "It is the key to a treasure found by a Gold-Bug in one corner."
poss_paddings[1] = "a Gold-Bug in one corner. It is the key to a treasure found by"
poss_paddings[2] = "It is the key to a treasure found by a Gold-Bug in one corner"
poss_paddings[3] = "Codagami: This door has RSA encryption with exponent 5 and the password is"
poss_paddings[4] = "This door has RSA encryption with exponent 5 and the password is"


for curr in poss_paddings:
    print(curr)
    try_poss_edits(curr)
    
    lowStr = curr.lower()
    print(lowStr)
    try_poss_edits(lowStr)
    
    highStr = curr.upper()
    print(highStr)
    try_poss_edits(highStr)









