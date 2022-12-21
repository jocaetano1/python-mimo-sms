# -*- coding: utf8 -*-

from setuptools import find_packages, setup


description = "MIMO SMS Gateway Python Library"

with open("README.md") as file:
    long_description = file.read()

setup(
    name="mimosms",
    version="1.0.2",
    author="João Santos",
    description=description,
    long_description=long_description,
    url="https://https://pypi.org/project/mimosms/",
    packages=find_packages(
        where='src/',
        include=['*'],
        exclude=['tests'],
    ),
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['gateway', 'sms', 'mimo'],
    python_requires=">=3.8",
    py_modules=["mimo_sms"],
    package_dir={"": "src"},
    maintainer="João Santos",
    author_email="josan5368@gmail.com"
)
