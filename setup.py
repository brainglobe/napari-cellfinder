#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


requirements = [
    "napari-plugin-engine >= 0.1.4",
    "imlib",
    "napari-ndtiffs",
    "napari-brainreg>=0.2.2",
]


# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "napari_cellfinder/_version.py"}

setup(
    name="napari-cellfinder",
    author="Adam Tyson",
    author_email="adam.tyson@ucl.ac.uk",
    license="MIT",
    url="https://github.com/brainglobe/napari-cellfinder",
    description="Visualise cellfinder results with napari",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
    use_scm_version=use_scm,
    setup_requires=["setuptools_scm"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: napari",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "napari.plugin": [
            "cellfinder = napari_cellfinder",
        ],
    },
)
