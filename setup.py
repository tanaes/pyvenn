#!/usr/bin/env python
# copied and modified from https://github.com/biocore/scikit-bio
from setuptools import find_packages, setup
from glob import glob

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pyvenn',
    version="0.0.0",
    description='Venn diagrams',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['matplotlib']
)
