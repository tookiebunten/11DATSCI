# def binary_multiply(binary1: list[int], binary2: list[int]) -> float:
#     """Receives two binary [0, 1] lists and returns, as a decimal, the result of 
#     multiplying those two numbers. Use a for loop to decode the binary strings, 
#     which must be the same length. """
#     if len(binary1) != len(binary2):
#         raise ValueError("Both binary numbers must have the same length.")

def list_to_binary_string(binary_list):
    return ''.join(str(bit) for bit in binary_list)

def binary_string_to_int(binary_string):
    return int(binary_string, 2)

if __name__ == "__main__":
    print(binary_string_to_int(list_to_binary_string([1, 0, 1, 0, 1, 0, 1, 0])))  # 170