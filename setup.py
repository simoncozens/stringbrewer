#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

config = {
    'name': 'stringbrewer',
    'author': 'Simon Cozens',
    'author_email': 'simon@simon-cozens.org',
    'url': 'https://github.com/simoncozens/stringbrewer',
    'description': 'Generate random strings matching a pattern',
    'long_description': open('README.md', 'r').read(),
    'long_description_content_type': 'text/markdown',
    'license': 'MIT',
    'version': '0.0.1',
    'install_requires': install_requires,
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"

    ],
    'package_dir': {'stringbrewer': 'stringbrewer'},
    'packages': find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
,
}

if __name__ == '__main__':
    setup(**config)
