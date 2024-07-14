from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='binaryconvert',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='A super easy Python tool that converts your text into binary language (8-bit).',
    author='wfxey',
    author_email='projectsdi02@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/wfxey/binaryconvert',
    download_url='https://github.com/wfxey/binaryconvert/archive/refs/tags/v1.0.tar.gz',
    keywords=['binary', '8-bit', 'text-to-binary'],
    install_requires=[
        # Empty
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',
)
