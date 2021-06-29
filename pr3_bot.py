import struct

E_SIZE = 1 + 8 + 1 + 2
D_SIZE = 4 + 2 + 4 + 2 * 7 + 2 + 2 + 1 * 7
C_SIZE = 2 + 2 + 2
B_SIZE = 4 + 1 + D_SIZE + 2
A_SIZE = 4 + 2 + 2 + 4 + 2 + 2


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset:offset+E_SIZE]
    e_parsed = struct.unpack('>BdBh', e_bytes)
    return {'E1': e_parsed[0], 'E2': e_parsed[1], 'E3': e_parsed[2], 'E4':e_parsed[3]}


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>iHIhhhhhhhHhBBBBBBB', d_bytes)
    d2_bytes = byte_string[d_parsed[2] : d_parsed[2] + d_parsed[1]]
    d2_parsed = struct.unpack('>'+'B'*d_parsed[1], d2_bytes)
    return {'D1': d_parsed[0],
            'D2': list(d2_parsed),
            'D3': list(d_parsed[3:10:]),
            'D4': d_parsed[10],
            'D5': d_parsed[11],
            'D6': list(d_parsed[12:])
            }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>HHH', c_bytes)
    c2_bytes = byte_string[c_parsed[1]: c_parsed[1] + c_parsed[0]]
    c2_parsed = struct.unpack('>'+'b' * c_parsed[0], c2_bytes)
    return {'C1': list(c2_parsed),
            'C2': c_parsed[2]
    }


def parse_b(offset, byte_string):
    b12_bytes = byte_string[offset:offset + 5]
    b12_parsed = struct.unpack('>IB', b12_bytes)
    #b3_parsed = parse_d(offset + 5, byte_string),
    b4_bytes = byte_string[offset + 5 + D_SIZE: offset + 5 + D_SIZE + 2]
    b4_parsed = struct.unpack('>'+'H', b4_bytes)
    #print(type(b3_parsed))
    return {'B1': parse_c(b12_parsed[0], byte_string),
            'B2': b12_parsed[1],
            'B3': parse_d(offset + 5, byte_string),#b3_parsed,
            'B4': parse_e(b4_parsed[0], byte_string)
    }

def parse_a(offset, byte_string):
    a_bytes = byte_string[offset:offset + A_SIZE]
    a_parsed = struct.unpack('>iHhIHH', a_bytes)
    a4_parsed = struct.unpack('>'+'I' * a_parsed[3], byte_string[a_parsed[4]:a_parsed[4]+a_parsed[3] * 4])
    a4_list_parsed = [parse_b(addr, byte_string) for addr in a4_parsed]
    return {'A1': a_parsed[0],
            'A2': a_parsed[1],
            'A3': a_parsed[2],
            'A4': a4_list_parsed,
            'A5': a_parsed[5]
            }

def f31(byte_string):
    return parse_a(5, byte_string)


print(f31(b'qKOEN\x963\xe0f\xb3O\x93\x85\x00\x00\x00\x02\x00\x99\xb6\x15{\xf0\t'
b'\xf9\xce\x00\x05\x00\x159\xff\xc4{\xe8\xfa\xbf\xda\xcff}\x86\x7f\x0c'
b')6\x92\x00\x00\x00\x1a\xf0\xd2\x1d\xdf\x81\x00\x03\x00\x00\x00 \x9e\x92'
b'\x19\xf2\\\x99?\xb8\xc7S\x98]\x80\xef\x8b,\xbf\x83B\x06\x03\x04\x96\x94{\x00'
b'#\xc3\xed\x00\x02\x00Y:\xa6\xdf\xe4/\xbf\xe00\xec\\$y\x18\xc0\xf5U\x00'
b'\x00\x00[\x1aSU\x95\xe5\x00\x02\x00\x00\x00a\x90\xf0\xffH\xa8b\n\xa9\xa6\x03'
b'n\x12\xbb\xd4\x1f\xa0\x83\x8d\xe0\x12\xa0d\xbe\xec\x1c\x00c\x00\x00\x00'
b'/\x00\x00\x00o'))



class C32:
    head = 'A'
    tab = {'A': [['B', 0], ['D', 1]], 'B': [[], ['C', 2]], 'C': [['E', 4], ['D', 3]],
           'D': [['G', 6], ['E', 5]], 'E': [['F', 7], []], 'F': [[],['G', 8]], 'G':[['E', 9], []]}

    def stare(self):
        try:
            a = (self.tab[self.head])[0][1]
            self.head = self.tab[self.head][0][0]
            return (a)
        except:
            return(None)

    def flip(self):
        try:
            a = (self.tab[self.head])[1][1]
            self.head = self.tab[self.head][1][0]
            return(a)
        except:
            return(None)
