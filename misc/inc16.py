def inc16(inpt: list):
    out = []
    carry = 1
    for bit in list(reversed(inpt)):
        out.append(bit ^ carry)
        carry = bit & carry 
        count += 1

    return list(reversed(out))

inpt = [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
print(inc16(inpt))


