from re import M
from setuptools import setup,find_packages

print(find_packages())
setup(
    name = "src",
    version="0.0.1",
    description="MLOps Pipeline for WinqQ",
    author="Rohan",
    packages=find_packages(),
    license="MIT"
)