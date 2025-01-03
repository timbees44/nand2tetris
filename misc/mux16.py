def mux16(a_bits, b_bits, sel):
    if len(a_bits) != 16 or len(b_bits) != 16:
        raise ValueError("both inputs need to be 16 bits (arrays of len 16)")

    out = [a_bits[bit] if sel == 0 else b_bits[bit] for bit in range(16)]

    return out

a_bits = [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1]
b_bits = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]

zero_sel = mux16(a_bits, b_bits, 0)

print("sel = 0")
print(a_bits)
print(b_bits)
print(zero_sel)
print("\n")

one_sel = mux16(a_bits, b_bits, 1)

print("sel = 1")
print(a_bits)
print(b_bits)
print(one_sel)

