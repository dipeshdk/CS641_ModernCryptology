import binascii

# Given RSA values
exp = 5
cipher = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693
n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
padding = "You see a Gold-Bug in one corner. It is the key to a treasure found by "

def roots_of_poly(padding):
    ZmodN = Zmod(n)
    _cipher = ZmodN(cipher)
    _exp = ZmodN(exp)
    _padding = ZmodN(padding)
    P.<x> = PolynomialRing(ZmodN)
    poly = (x + _padding )^_exp - _cipher
    poly = poly.monic()
    root = poly.small_roots()
    return root


def convert_padding(_padding):
    bytes_utf8 = bytes(_padding, 'utf-8')
    hex_padding = binascii.hexlify(bytes_utf8)
    int_padding = int(hex_padding, 16)
    return int_padding


def break_RSA():
    _padding = padding
    for i in range(0, 25, 1):
        int_padding = convert_padding(_padding)
        roots = roots_of_poly(int_padding)
        if len(roots):
            res = Integer(roots[0])
            ans = hex(res)
            print("Yay! Password found!")
            print(f'Password : {binascii.unhexlify(ans[2:]).decode("utf-8")}')
            return
        else:
            _padding = _padding + '\x00'
    print("Password not found :(")


break_RSA()