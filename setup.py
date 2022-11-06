from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="exceltocsv",
    version="0.0.1",
    author="Simo Piitulainen",
    author_email="simopiitulainen@outlook.com",
    description="A package to convert excel files to csv",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/simopiitulainen/exceltocsv",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)