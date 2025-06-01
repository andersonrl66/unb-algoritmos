def lcs(x, y):
    table = {}
    return lcfR(x, y, len(x), len(y), table)

def lcfR(x, y, i, j, table):
    assert i >= 0
    assert j >= 0
    if (i,j) in table:
        return table[(i, j)]
    elif i == 0 or j == 0:
        res = 0
    elif x[i-1] == y[j-1]:
        res = lcfR(x, y, (i-1), (j-1), table) + 1
    else:
        res = max(lcfR(x, y, (i-1), j, table), lcfR(x, y, i, (j-1), table))
    table[(i,j)] = res
    return res


s1 = "ABCBDAB"
s2 = "BDCABA"

print(lcs(s1, s2))
