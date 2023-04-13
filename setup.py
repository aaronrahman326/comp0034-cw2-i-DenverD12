"""This file contains setup details for the project and app."""
from setuptools import setup, find_packages

setup(
    name="comp0034-cw1-i-DenverD12",
    author="Denver D'Silva",
    url="https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12",
    python_requires=">=3.10",
    packages=find_packages(include=[]),
    install_requires=[
        "flask",
        "flask-marshmallow",
        "flask-sqlalchemy",
        "flask-wtf",
        "jwt",
        "marshmallow-sqlalchemy",
        "openpyxl",
        "pandas",
        "requests",
        "scikit-learn",
    ],
    package_data={
        "Tourism_arrivals_prepared": ["Tourism_arrivals_prepared.csv"],
    },
)
