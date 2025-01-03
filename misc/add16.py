def add16(a: list, b: list) -> tuple[list, int]:
    out = []
    c = 0
    for bit_a, bit_b in zip(a, b)
        c = (bit_a & bit_b) | (bit_b & c) | (bit_a & c)
        out.append(bit_a ^ bit_b ^ c)

    return out, c

a = [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
b = [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]

result_sum, result_carry = add16(a, b)
print(f"Sum: {result_sum}, Carry: {result_carry}")
