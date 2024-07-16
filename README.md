# BinaryConvert

![PyPI - Downloads](https://img.shields.io/pypi/dm/binaryconvert)

A super easy Python tool that converts your text into binary language (8-bit).

## Installation

```bash
pip install binaryconvert
```
# Example

<hr>

## ToBinary()

```python
from binaryconvert import convert

convert.ToBinary("Hi, my name is wfxey!")
```
### Output
```bash
01001000 01100001 01100001 01101100 01100001 01101100 01101100 01100001 01100001 01101111
```
<hr>

## ToText()

```python
from binaryconvert import convert

convert.ToText("01001000 01100001 01100001 01101100 01100001 01101100 01101100 01100001 01100001 01101111")
```
### Output
```bash
Hi, my name is wfxey!
```

<hr>

# CLI Usage

BinaryConvert also provides a command line interface (CLI) for easy conversion without writing a single line of Python code.

## ToBinary Command

Convert normal text to binary (8-bit) using the to_binary command.

```bash
python -m binaryconvert to_binary "Hi, my name is wfxey!"
```
### Output
```bash
01001000 01101001 00101100 00100000 01101101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01110111 01100110 01111000 01100101 01111001 00100001
```
## ToText Command

Convert binary (8-bit) to normal text using the to_text command.

```bash
python -m binaryconvert to_text "01001000 01101001 00101100 00100000 01101101 01111001 00100000 01101110 01100001 01101101 01100101 00100000 01101001 01110011 00100000 01110111 01100110 01111000 01100101 01111001 00100001"
```
### Output
```bash
Hi, my name is wfxey!
```

