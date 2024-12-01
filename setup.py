from setuptools import find_packages, setup
from typing import List


def parse_long_description(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()

def parse_requirements(filepath: str) -> List[str]:
    with open(filepath, "r") as file:
        return [
            line for line in file if line and not line.startswith("#")
        ]


setup(
    name="pyetrade",
    version="0.0.01",
    description="A package for interacting with the E*TRADE API",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=parse_long_description("app/README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/AakshRanjan/pyEtrade.git",
    author="Aaksh Ranjan",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=parse_requirements("requirements.in"),
    python_requires=">=3.10",
)