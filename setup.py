# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import re

marlin = os.path.join("marlin", "scripts", "marlin.bat")

with open("README.md") as f:
    readme = f.read()


with open("marlin/__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)


setup(
    name="bookmark",
    version=version,
    description="Swim between bookmarks in the terminal",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Jitendra",
    author_email="jitendra.rl.2001@gmail.com",
    url="https://github.com/Jitendra0101/bookmark",
    license="None",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=["click", "colorama"],
    python_requires=">=3",
    scripts=[marlin],
    entry_points={
        "console_scripts": [
            "bookmark = marlin.bookmark:main",
            "rmark = marlin.rmark:main",
            "marlin_help = marlin.marlin_help:main",
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
