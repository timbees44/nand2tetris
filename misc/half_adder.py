def half_adder(a: int, b: int) -> tuple[int, int]:
    sum_ = a ^ b # bitwise OR
    carry = a & b # bitwise AND
    return sum_, carry 

a, b = 1, 1
result_sum, result_carry = half_adder(a, b)
print(f"Sum: {result_sum}, Carry: {result_carry}")
