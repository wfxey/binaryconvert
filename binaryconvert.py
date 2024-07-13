def convert(text):
    for char in text:
        binary_char = format(ord(char), '08b')
        print(binary_char)