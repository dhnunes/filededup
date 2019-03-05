from distutils.core import setup
from setuptools import find_packages

setup(
    name="Python-Deduplicator",
    author="Diogo Nunes",
    author_email="diogo.hap@gmail.com",
    url="https://github.com/dhnunes/pdedup",
    version="1.0.0.dev1",
    packages=find_packages(),
    license="GPL-V3",
    long_description=open("README.md").read(),
    scripts=[
        "bin/pdedup",
    ],
    install_requires=[
        "tqdm==4.29.1",
        "reprint==0.5.2",
    ],
)
