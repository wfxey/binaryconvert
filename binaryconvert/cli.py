import click
from .convert import (
    To_Binary, To_Text, To_Hex, From_Hex, To_Decimal, From_Decimal,
    Reverse_Text, To_Base64, From_Base64, Is_Palindrome, Count_Characters,
    To_LeetSpeak, To_MorseCode, From_MorseCode
)

@click.group()
def cli():
    """Binaryconvert CLI library."""
    pass

@click.command()
@click.argument('text')
@click.argument('bit', type=int)
def to_binary(text, bit):
    """Convert text to binary representation."""
    try:
        binary_result = To_Binary(text, bit)
        click.echo(binary_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('binary')
def to_text(binary):
    """Convert binary to text."""
    try:
        text_result = To_Text(binary)
        click.echo(text_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def to_hex(text):
    """Convert text to hexadecimal representation."""
    try:
        hex_result = To_Hex(text)
        click.echo(hex_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('hex_string')
def from_hex(hex_string):
    """Convert hexadecimal to text."""
    try:
        text_result = From_Hex(hex_string)
        click.echo(text_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def to_decimal(text):
    """Convert text to decimal representation."""
    try:
        decimal_result = To_Decimal(text)
        click.echo(decimal_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('decimal_string')
def from_decimal(decimal_string):
    """Convert decimal to text."""
    try:
        text_result = From_Decimal(decimal_string)
        click.echo(text_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def reverse_text(text):
    """Reverse the input text."""
    try:
        reversed_result = Reverse_Text(text)
        click.echo(reversed_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def to_base64(text):
    """Encode text to Base64."""
    try:
        base64_result = To_Base64(text)
        click.echo(base64_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('base64_string')
def from_base64(base64_string):
    """Decode Base64 to text."""
    try:
        text_result = From_Base64(base64_string)
        click.echo(text_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def is_palindrome(text):
    """Check if the text is a palindrome."""
    try:
        result = Is_Palindrome(text)
        click.echo(f"Is Palindrome: {result}")
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def count_characters(text):
    """Count character frequency in the text."""
    try:
        char_count = Count_Characters(text)
        click.echo(char_count)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def to_leetspeak(text):
    """Convert text to leetspeak."""
    try:
        leetspeak_result = To_LeetSpeak(text)
        click.echo(leetspeak_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('text')
def to_morsecode(text):
    """Convert text to Morse code."""
    try:
        morse_result = To_MorseCode(text)
        click.echo(morse_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('morse_code')
def from_morsecode(morse_code):
    """Convert Morse code to text."""
    try:
        text_result = From_MorseCode(morse_code)
        click.echo(text_result)
    except ValueError as e:
        click.echo(f"Error: {e}")

cli.add_command(to_binary)
cli.add_command(to_text)
cli.add_command(to_hex)
cli.add_command(from_hex)
cli.add_command(to_decimal)
cli.add_command(from_decimal)
cli.add_command(reverse_text)
cli.add_command(to_base64)
cli.add_command(from_base64)
cli.add_command(is_palindrome)
cli.add_command(count_characters)
cli.add_command(to_leetspeak)
cli.add_command(to_morsecode)
cli.add_command(from_morsecode)

if __name__ == "__main__":
    cli()