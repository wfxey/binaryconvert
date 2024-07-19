def ToBinary(text, bit):
    binary_list = []
    for char in text:
        binary_char = format(ord(char), f'0{bit}b')
        binary_list.append(binary_char)
    return ' '.join(binary_list)

def ToText(binary):
    binary_values = binary.split()
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)

if __name__ == "__main__":
    binary_output = ToBinary("Hi, my name is wfxey!", 8)
    print(binary_output)
    
    text_output = ToText("01001000 01101001 00101100 00100000 01101101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01110111 01100110 01111000 01100101 01111001 00100001")
    print(text_output)
