def bin_to_dec(binary_str: str) -> int:
    decimal_value = 0
    length = len(binary_str)

    for i, digit in enumerate(binary_str):
        power = length - i - 1
        if digit == "1":
            decimal_value += 2 ** power
        
    return decimal_value
        

binary_input = "100110011"
decimal_output = bin_to_dec(binary_input)
print(f"Binary: {binary_input} -> Decimal: {decimal_output}")
