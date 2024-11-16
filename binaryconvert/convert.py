def To_Binary(text: str, bit: int) -> str:
    if not text:
        raise ValueError("Input text cannot be empty.")
    if bit <= 0:
        raise ValueError("Bit value must be greater than 0.")
    return ' '.join(format(ord(char), f'0{bit}b') for char in text)

def To_Text(binary: str) -> str:
    if not binary:
        raise ValueError("Binary input cannot be empty.")
    try:
        return ''.join(chr(int(bv, 2)) for bv in binary.split())
    except ValueError as e:
        raise ValueError(f"Invalid binary input: {binary}. Error: {e}")

if __name__ == "__main__":
    try:
        binary_output = To_Binary("Hi, my name is wfxey!", 8)
        print(f"Binary Output: {binary_output}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        text_output = To_Text("01001000 01101001 00101100 00100000 01101101 01111001 00100000 "
                              "01101110 01100001 01101101 01100101 00100000 01101001 01110011 "
                              "00100000 01110111 01100110 01111000 01100101 01111001 00100001")
        print(f"Text Output: {text_output}")
    except ValueError as e:
        print(f"Error: {e}")
