# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
        name = "pyie",
        version = '0.1.2',
        description = "Validador de Inscrição Estadual para Python",
        license = "MIT",
        author = "Fabiano Moraes",
        author_email = "fabiano.moraes@outlook.com",
        url = "https://github.com/famoraes/pyie",
        packages = find_packages(exclude = ['tests']),
        keywords = "python inscrição estadual ie",
        zip_safe = True
    )