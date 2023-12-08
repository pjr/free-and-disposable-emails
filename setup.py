import sys
from setuptools import setup, find_packages

# Importlib-resources is needed with python under 3.9
install_requires = []
if sys.version_info < (3, 9):
    install_requires.append("importlib-resources")

setup(
    name="freemailchecker",
    version="0.1.1",
    author="Philip Reynolds",
    author_email="philip.reynolds@gmail.com",
    description="A simple python package which checks for the domain in a list of free and disposable email domains. Includes gmail.com and mailinator.com style",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pjr/freemailchecker",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    # If you have package data such as CSV files or templates, include them here
    package_data={
        "freemailchecker": ["data/*.csv"],
    },
    install_requires=install_requires,
    # If you want to include non-code files (like the README.md), specify them here
    include_package_data=True,
    test_suite="tests",
)
