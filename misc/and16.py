def and16(a_bits, b_bits):
    if len(a_bits) != 16 or len(b_bits) != 16:
        raise ValueError("Input must be 16 bits!")
    
    return [a_bits[bit] & b_bits[bit] for bit in range(0,16)]

a_bits = [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1]
b_bits = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]

output = and16(a_bits, b_bits)
print("Original")
print(a_bits)
print(b_bits)
print(output)
print("\n")

## zip implementation
def zip_and16(a_bits, b_bits):
    if len(a_bits) != 16 or len(b_bits) != 16:
        raise ValueError("Input must be 16 bits!")
    
    return [abit & bbit for abit, bbit in zip(a_bits, b_bits)]

a_bits = [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1]
b_bits = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]

output = zip_and16(a_bits, b_bits)
print("Using zip")
print(a_bits)
print(b_bits)
print(output)
print("\n")
