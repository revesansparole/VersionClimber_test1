#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from setuptools import setup, find_packages


short_descr = "belle petite description"
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


# find version number in src/VersionClimber_test1/version.py
version = {}
with open("src/VersionClimber_test1/version.py") as fp:
    exec(fp.read(), version)


setup_kwds = dict(
    name='VersionClimber_test1',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="moi",
    author_email="moi@email.com",
    url='https://github.com/moi/VersionClimber_test1',
    license='cecill-c',
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=[
        "pytest-runner",
        ],
    install_requires=[
        ],
    tests_require=[
        "coverage",
        "mock",
        "pytest",
        "pytest-cov",
        ],
    entry_points={},
    keywords='',
    )
# #}
# change setup_kwds below before the next pkglts tag

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
