from collections import Counter

def f21(tree):
    answ = ['stan',1, 'golo', 2, 1970, 0, 2006, 3, 1963, 4, 1958, 5, 1974, 7,1964, 8, 1959, 9]
    if (tree[4]=='alloy'):
        if (tree[0]=='smali'):return 6
        else: return answ[answ.index(tree[3]+1)+1]
    elif (tree[3]==1973):
        if (tree[2]!=1987): return answ[answ.index(tree[2])+1]
        else: return answ[answ.index(tree[1])+1]
    else: return answ[answ.index(tree[3])+1]

def f22(x):
    xx = bin(x)
    A = str(bin((x & 0b111111111))[2:]).zfill(9)
    B = str(bin((x & 0b111111000000000) >> 9)[2:]).zfill(6)
    C = str(bin((x & 0b1111111000000000000000) >> 15)[2:]).zfill(7)
    D = str(bin((x & 0b110000000000000000000000) >> 22)[2:]).zfill(2)
    E = str(bin((x & 0b11111000000000000000000000000) >> 24)[2:]).zfill(5)
    F = str(bin((x & 0b1100000000000000000000000000000) >> 29)[2:]).zfill(2)
    G = str(bin((x & 0b10000000000000000000000000000000) >> 31)[2:]).zfill(1)
    return (int("0b" + A + B + D + F + G + E + C, 2))

def f23(table):
    table_2 = []
    for i in range (len(table)):
        table_2.append(list(Counter(table[i])))

    for i in range (len(table)):
        table_2[i][0] = table_2[i][0].replace('@', '[at]')
        date = table_2[i][2].split('-')
        table_2[i][2] = (date[2]+'/'+ date[1]+'/'+date[0])
        table_2[i][1] = table_2[i][1].split()[1] + ' ' + table_2[i][1][0] + '.'
        table_2[i][3] = "%.2f" % (float(table_2[i][3])) #str(round(float(table_2[i][3]), 2))
    return table_2
