from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Punjabi programming utilities for python'
LONG_DESCRIPTION = 'Python utility functions for working with the Punjabi language for basic text processing or more sophisticated NLP tasks'

setup(
    name="punjabi",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="hgcd",
    author_email="harkiratg@cosmodigital.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='punjabi',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)