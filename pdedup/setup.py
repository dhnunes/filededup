from setuptools import setup, find_packages

setup( 
    name="pdedup",
    version="0.1",
    description="File Deduplication and file operations",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Topic :: File Processing :: File Handling",
    ],
    author="Diogo Nunes",
    author_email="diogo.hap@gmail.com",
    packages=find_packages(),
    scripts=["pdedup/bin/pdedup"],
)