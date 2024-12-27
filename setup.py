from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    requirements = []

setup(
    name='binaryconvert',
    version='3.0.0',
    packages=find_packages(),
    license='MIT',
    description='A Python tool that converts text to binary and other formats like hexadecimal, Base64, Morse code, and more!',
    author='wfxey',
    author_email='velis.help@web.de',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/wfxey/binaryconvert',
    download_url='https://github.com/wfxey/binaryconvert/archive/refs/tags/v3.0.0.tar.gz',
    keywords=[
        'binary', 'binaries', 'text-to-binary', 'hexadecimal', 'base64', 
        'morse-code', 'utilities', 'converter'
    ],
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'flake8>=4.0.0'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'binaryconvert-cli=binaryconvert.cli:cli',
        ]
    },
    project_urls={
        'Documentation': 'https://github.com/wfxey/binaryconvert#readme',
        'Source': 'https://github.com/wfxey/binaryconvert',
        'Bug Tracker': 'https://github.com/wfxey/binaryconvert/issues',
    }
)