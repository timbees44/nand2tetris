def dmux(in_sig, sel):
    out_a = in_sig if sel == 0 else 0
    out_b = in_sig if sel == 1 else 0
    return out_a, out_b


def dmux4way(in_sig, sel):
    sel1, sel0 = sel[1], sel[0]

    ab, cd = dmux(in_sig, sel1)

    a, b = dmux(ab, sel0)
    c, d = dmux(cd, sel0)

    return a, b, c, d

in_sig = 1
sel = [1, 0]

a, b, c, d = dmux4way(in_sig, sel)
print(f"a: {a}, b: {b}, c: {c}, d: {d}")
