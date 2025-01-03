from typing import List

class alu():
    def __init__(self):
        pass

    # get integer using bitwise shift
    def _to_integer(self, bits: List[int]) -> int:
        return sum(bit << i for i, bit in enumerate(bits))

    # get integer using power of
    def _alt_to_integer(self, bits: List[int]) -> int:
        return sum(bit*2**i for i, bit in enumerate(bits))

    def _to_bits(self, value: int) -> List[int]:
        return [(value >> i) & 1 for i in range(16)]

    def zero_input(self, x: List[int], zx: bool) -> List[int]:
        return [0] * 16 if zx else x

    def negate_input(self, x: List[int], nx: bool) -> List[int]:
        if not nx:
            return x
        return self._to_bits(self._to_integer(x) ^ 0xFFFF)

    def add(self, x: List[int], y: List[int]) -> List[int]:
        return self._to_bits(self._to_integer(x) + self._to_integer(y))

    def and_operation(self, x: List[int], y: List[int]) -> List[int]:
        return [bit_x & bit_y for bit_x, bit_y in zip(x, y)]

    def compute(self, x: List[int], y: List[int], zx: bool, nx: bool, zy: bool, ny: bool, f: bool) -> List[int]:
        """Computes the ALU output based on the inputs."""
        x = self.zero_input(x, zx)
        x = self.negate_input(x, nx)
        y = self.zero_input(y, zy)
        y = self.negate_input(y, ny)

        if f:
            return self.add(x, y)  # f is 1 for addition
        else:
            return self.and_operation(x, y)  # f is 0 for AND

# Example of how to use the ALU class
alu = ALU()
x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1]  # Represents the number 85
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # Represents the number 63
result = alu.compute(x=x, y=y, zx=False, nx=False, zy=False, ny=False, f=True)
print(f"Result (as bits): {result}")


