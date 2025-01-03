def not16(input_arr):
    if len(input_arr) != 16:
        raise ValueError("Input needs to be 16bits")
    return [~bit & 1 for bit in input_arr]

input_arr = [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1]
output_arr = not16(input_arr)
print(output_arr)
