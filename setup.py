from setuptools import setup, find_packages

setup(
    name="comp0034-cw1-i-DenverD12",
    version="1.0.0",
    author="Denver D'Silva",
    url="https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12",
    python_requires=">=3.10",
    packages=find_packages(include=[]),
    install_requires=[
        "pandas",
        "openpyxl",
        "flask",
        "flask-sqlalchemy",
        "flask-wtf",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "numpy",
        "scikit-learn",
        "jwt",
        "requests",
    ],
    package_data={
        "Tourism_arrivals_prepared": ["Tourism_arrivals_prepared.csv"],
    },
)
