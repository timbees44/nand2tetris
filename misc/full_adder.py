def full_adder(a: int, b: int, c: int) -> tuple[int, int]:
    inpt = [a, b, c]
    carry = 1 if (inpt.count(1) == 2 or inpt.count(1) == 3) else 0
    sum_ = 1 if (inpt.count(1) == 1 or inpt.count(1) == 3) else 0

    return carry, sum_

def full_adder_refined(a: int, b: int, c: int) -> tuple[int, int]:
    carry = (a & b) | (b & c) | (a & c)
    sum_ = a ^ b ^ c

    return carry, sum_

a, b, c = 1, 0, 1
result_sum, result_carry = full_adder(a, b, c)
print(f"Sum: {result_sum}, Carry: {result_carry}")
