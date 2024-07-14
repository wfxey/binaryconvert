# BinaryConvert
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
