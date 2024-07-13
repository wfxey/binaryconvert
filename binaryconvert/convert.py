def binary(text):
    for char in text:
        binary_char = format(ord(char), '08b')
        print(binary_char)

if __name__ == "__main__":
    binary("Hi, my name is wfxey!")