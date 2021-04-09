︠73732ea0-de54-46f3-9af7-065310bfc72bs︠
def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):

    dd = pol.degree()
    nn = dd * mm + tt

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)

    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
#     print("lol")

    # test roots
    roots = []
#     print("lol")
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693

# RSA known parameters
ZmodN = Zmod(N);

def break_RSA(p_str, max_length_M):
    global e, C, ZmodN

    p_binary_str = ''.join(['{0:08b}'.format(ord(x)) for x in p_str])

    for length_M in range(0, max_length_M+1, 4):          # size of the root
#         print("here")

              # Problem to equation (default)
        P.<M> = PolynomialRing(ZmodN) #, implementation='NTL')
        pol = ((int(p_binary_str, 2)<<length_M) + M)^e - C
        dd = pol.degree()

        # Tweak those
        beta = 1
        epsilon = beta / 7
        mm = ceil(beta**2 / (dd * epsilon))
        tt = floor(dd * mm * ((1/beta) - 1))
        XX = ceil(N**((beta**2/dd) - epsilon))

        roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

        if roots:
            print("Root is :", ' {0:b}'.format(roots[0]))
            return

    print('No solution found')

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
poss_paddings = [0]*6
poss_paddings[0] = "It is the key to a treasure found by a Gold-Bug in one corner."
poss_paddings[1] = "a Gold-Bug in one corner. It is the key to a treasure found by"
poss_paddings[2] = "It is the key to a treasure found by a Gold-Bug in one corner"
poss_paddings[3] = "Codagami: This door has RSA encryption with exponent 5 and the password is"
poss_paddings[4] = "This door has RSA encryption with exponent 5 and the password is"
poss_paddings[5] = "	Codagami: This door has RSA encryption with exponent 5 and the password is"

for curr in poss_paddings:
    print(curr)
    try_poss_edits(curr)

    lowStr = curr.lower()
    print(lowStr)
    try_poss_edits(lowStr)

    highStr = curr.upper()
    print(highStr)
    try_poss_edits(highStr)
print("done")
︡4ca3e197-f389-4af4-99a8-d1f4cb3cab53︡{"stdout":"It is the key to a treasure found by a Gold-Bug in one corner.\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nit is the key to a treasure found by a gold-bug in one corner.\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nIT IS THE KEY TO A TREASURE FOUND BY A GOLD-BUG IN ONE CORNER.\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\na Gold-Bug in one corner. It is the key to a treasure found by\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\na gold-bug in one corner. it is the key to a treasure found by\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nA GOLD-BUG IN ONE CORNER. IT IS THE KEY TO A TREASURE FOUND BY\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nIt is the key to a treasure found by a Gold-Bug in one corner\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nit is the key to a treasure found by a gold-bug in one corner\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nIT IS THE KEY TO A TREASURE FOUND BY A GOLD-BUG IN ONE CORNER\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nCodagami: This door has RSA encryption with exponent 5 and the password is\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\ncodagami: this door has rsa encryption with exponent 5 and the password is\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nCODAGAMI: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nThis door has RSA encryption with exponent 5 and the password is\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nthis door has rsa encryption with exponent 5 and the password is\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nTHIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\n\tCodagami: This door has RSA encryption with exponent 5 and the password is\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\n\tcodagami: this door has rsa encryption with exponent 5 and the password is\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\n\tCODAGAMI: THIS DOOR HAS RSA ENCRYPTION WITH EXPONENT 5 AND THE PASSWORD IS\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\nNo solution found"}︡{"stdout":"\n"}︡{"stdout":"done\n"}︡{"done":true}︡









