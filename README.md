
# BinaryConvert CLI Library

This library provides a Command-Line Interface (CLI) for converting text between various encoding formats, including binary, hexadecimal, decimal, Base64, Morse code, leetspeak, and more.

## Available Commands

### `to_binary <text> <bit>`
Convert text to its binary representation.

Example:
```bash
$ python cli.py to_binary "Hello World" 8
```

### `to_text <binary>`
Convert binary to text.

Example:
```bash
$ python cli.py to_text "01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100"
```

### `to_hex <text>`
Convert text to hexadecimal representation.

Example:
```bash
$ python cli.py to_hex "Hello World"
```

### `from_hex <hex_string>`
Convert hexadecimal string to text.

Example:
```bash
$ python cli.py from_hex "48 65 6c 6c 6f 20 57 6f 72 6c 64"
```

### `to_decimal <text>`
Convert text to decimal representation.

Example:
```bash
$ python cli.py to_decimal "Hello World"
```

### `from_decimal <decimal_string>`
Convert decimal string to text.

Example:
```bash
$ python cli.py from_decimal "72 101 108 108 111 32 87 111 114 108 100"
```

### `reverse_text <text>`
Reverse the input text.

Example:
```bash
$ python cli.py reverse_text "Hello World"
```

### `to_base64 <text>`
Encode text to Base64.

Example:
```bash
$ python cli.py to_base64 "Hello World"
```

### `from_base64 <base64_string>`
Decode Base64 string to text.

Example:
```bash
$ python cli.py from_base64 "SGVsbG8gV29ybGQ="
```

### `is_palindrome <text>`
Check if the text is a palindrome.

Example:
```bash
$ python cli.py is_palindrome "A man a plan a canal Panama"
```

### `count_characters <text>`
Count the frequency of each character in the text.

Example:
```bash
$ python cli.py count_characters "Hello World"
```

### `to_leetspeak <text>`
Convert text to leetspeak.

Example:
```bash
$ python cli.py to_leetspeak "Hello World"
```

### `to_morsecode <text>`
Convert text to Morse code.

Example:
```bash
$ python cli.py to_morsecode "Hello World"
```

### `from_morsecode <morse_code>`
Convert Morse code to text.

Example:
```bash
$ python cli.py from_morsecode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

## Requirements

- Python 3.x
- `click` library (install using `pip install click`)

## Installation

1. Clone or download the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the CLI using:
   ```bash
   python cli.py <command> <args>
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.