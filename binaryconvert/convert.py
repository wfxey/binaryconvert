def To_Binary(text: str, bit: int = 8) -> str:
    """Convert text to binary representation.

    Args:
        text (str): The input text to convert.
        bit (int): Number of bits for each character's binary representation.

    Returns:
        str: Space-separated binary representation of the input text.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    if bit <= 0:
        raise ValueError("Bit value must be greater than 0.")

    return ' '.join(format(ord(char), f'0{bit}b') for char in text)

def To_Text(binary: str) -> str:
    """Convert binary representation back to text.

    Args:
        binary (str): Space-separated binary string.

    Returns:
        str: Decoded text from the binary input.

    Raises:
        ValueError: If input is invalid.
    """
    if not binary:
        raise ValueError("Binary input cannot be empty.")
    try:
        return ''.join(chr(int(bv, 2)) for bv in binary.split())
    except ValueError as e:
        raise ValueError(f"Invalid binary input: {binary}. Error: {e}")

def To_Hex(text: str) -> str:
    """Convert text to hexadecimal representation.

    Args:
        text (str): The input text to convert.

    Returns:
        str: Space-separated hexadecimal representation of the input text.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")

    return ' '.join(format(ord(char), '02x') for char in text)

def From_Hex(hex_string: str) -> str:
    """Convert hexadecimal representation back to text.

    Args:
        hex_string (str): Space-separated hexadecimal string.

    Returns:
        str: Decoded text from the hexadecimal input.

    Raises:
        ValueError: If input is invalid.
    """
    if not hex_string:
        raise ValueError("Hexadecimal input cannot be empty.")
    try:
        return ''.join(chr(int(h, 16)) for h in hex_string.split())
    except ValueError as e:
        raise ValueError(f"Invalid hexadecimal input: {hex_string}. Error: {e}")

def To_Decimal(text: str) -> str:
    """Convert text to decimal representation.

    Args:
        text (str): The input text to convert.

    Returns:
        str: Space-separated decimal representation of the input text.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")

    return ' '.join(str(ord(char)) for char in text)

def From_Decimal(decimal_string: str) -> str:
    """Convert decimal representation back to text.

    Args:
        decimal_string (str): Space-separated decimal string.

    Returns:
        str: Decoded text from the decimal input.

    Raises:
        ValueError: If input is invalid.
    """
    if not decimal_string:
        raise ValueError("Decimal input cannot be empty.")
    try:
        return ''.join(chr(int(d)) for d in decimal_string.split())
    except ValueError as e:
        raise ValueError(f"Invalid decimal input: {decimal_string}. Error: {e}")

def Reverse_Text(text: str) -> str:
    """Reverse the input text.

    Args:
        text (str): The input text to reverse.

    Returns:
        str: Reversed text.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    return text[::-1]

def To_Base64(text: str) -> str:
    """Encode text to Base64 format.

    Args:
        text (str): The input text to encode.

    Returns:
        str: Base64-encoded string.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    import base64
    return base64.b64encode(text.encode()).decode()

def From_Base64(base64_string: str) -> str:
    """Decode Base64 string back to text.

    Args:
        base64_string (str): The Base64-encoded string.

    Returns:
        str: Decoded text.

    Raises:
        ValueError: If input is invalid.
    """
    if not base64_string:
        raise ValueError("Base64 input cannot be empty.")
    import base64
    try:
        return base64.b64decode(base64_string.encode()).decode()
    except Exception as e:
        raise ValueError(f"Invalid Base64 input: {base64_string}. Error: {e}")

def Is_Palindrome(text: str) -> bool:
    """Check if the input text is a palindrome.

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

def Count_Characters(text: str) -> dict:
    """Count the frequency of each character in the input text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    from collections import Counter
    return dict(Counter(text))

def To_LeetSpeak(text: str) -> str:
    """Convert text to leetspeak.

    Args:
        text (str): The input text to convert.

    Returns:
        str: Text converted to leetspeak.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    leet_dict = {
        'a': '4', 'b': '8', 'c': '<', 'd': '|)', 'e': '3', 'f': '|=',
        'g': '6', 'h': '#', 'i': '1', 'j': '_|', 'k': '|<', 'l': '|_',
        'm': '|\/|', 'n': '|\|', 'o': '0', 'p': '|>', 'q': '0,', 'r': '|2',
        's': '5', 't': '7', 'u': '|_|', 'v': '\/', 'w': '\\/\\/', 'x': '}{',
        'y': '`/', 'z': '2'
    }
    return ''.join(leet_dict.get(char.lower(), char) for char in text)

def To_MorseCode(text: str) -> str:
    """Convert text to Morse code representation.

    Args:
        text (str): The input text to convert.

    Returns:
        str: Space-separated Morse code representation of the input text.

    Raises:
        ValueError: If input is invalid.
    """
    if not text:
        raise ValueError("Input text cannot be empty.")
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/'
    }
    return ' '.join(morse_dict.get(char.lower(), '?') for char in text)

def From_MorseCode(morse_code: str) -> str:
    """Convert Morse code representation back to text.

    Args:
        morse_code (str): Space-separated Morse code string.

    Returns:
        str: Decoded text from the Morse code input.

    Raises:
        ValueError: If input is invalid.
    """
    if not morse_code:
        raise ValueError("Morse code input cannot be empty.")
    morse_dict = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '/': ' '
    }
    try:
        return ''.join(morse_dict.get(code, '?') for code in morse_code.split())
    except Exception as e:
        raise ValueError(f"Invalid Morse code input: {morse_code}. Error: {e}")

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

    try:
        hex_output = To_Hex("Hi, my name is wfxey!")
        print(f"Hexadecimal Output: {hex_output}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        text_from_hex = From_Hex("48 69 2c 20 6d 79 20 6e 61 6d 65 20 69 73 20 77 66 78 65 79 21")
        print(f"Text from Hexadecimal: {text_from_hex}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        decimal_output = To_Decimal("Hi, my name is wfxey!")
        print(f"Decimal Output: {decimal_output}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        text_from_decimal = From_Decimal("72 105 44 32 109 121 32 110 97 109 101 32 105 115 32 119 102 120 101 121 33")
        print(f"Text from Decimal: {text_from_decimal}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        reversed_text = Reverse_Text("Hi, my name is wfxey!")
        print(f"Reversed Text: {reversed_text}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        base64_output = To_Base64("Hi, my name is wfxey!")
        print(f"Base64 Output: {base64_output}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        text_from_base64 = From_Base64("SGksIG15IG5hbWUgaXMgd2Z4ZXkh")
        print(f"Text from Base64: {text_from_base64}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        is_palindrome = Is_Palindrome("A man a plan a canal Panama")
        print(f"Is Palindrome: {is_palindrome}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        char_count = Count_Characters("Hi, my name is wfxey!")
        print(f"Character Count: {char_count}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        leetspeak_output = To_LeetSpeak("Hi, my name is wfxey!")
        print(f"Leetspeak Output: {leetspeak_output}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        morse_output = To_MorseCode("Hi, my name is wfxey!")
        print(f"Morse Code Output: {morse_output}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        text_from_morse = From_MorseCode(".... .. --..-- / -- -.-- / -. .- -- . / .. ... / .-- ..-. -..- . -.-- -.-.--")
        print(f"Text from Morse Code: {text_from_morse}")
    except ValueError as e:
        print(f"Error: {e}")