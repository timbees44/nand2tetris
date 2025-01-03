def mux4way16(a, b, c, d, sel):
    if not all(isinstance(x, list) and len(x) == 16 for x in [a, b, c,d ]):
        raise ValueError("inputs must be lists of 16 integers") 

    if not (isinstance(sel, tuple) and len(sel) == 2 and all(isinstance(x, int) for x in sel)):
        raise ValueError("inputs must be lists of 16 integers") 

    if sel[0] == 0:
        if sel[1] == 0:
            return a
        else:
            return b
    else:
        if sel[1] == 0:
            return c
        else:
            return d

a = [0]*16
b = [1]*16
c = [2]*16
d = [3]*16

# e.g.
sel = (1, 1)
output = mux4way16(a, b, c, d, sel)
print("Selected output:", output)


