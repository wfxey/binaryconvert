import click
from .convert import ToBinary, ToText

@click.group()
def cli():
    """Binaryconvert CLI library."""
    pass

@click.command()
@click.argument('text', 'bit')
def to_binary(text, bit):
    """Convert normal text to binary (8-bit)."""
    binary_result = ToBinary(text, bit)
    click.echo(binary_result)

@click.command()
@click.argument('binary')
def to_text(binary):
    """Convert binary (8-bit) to normal text."""
    text_result = ToText(binary)
    click.echo(text_result)

cli.add_command(to_binary)
cli.add_command(to_text)
