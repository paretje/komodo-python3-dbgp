#!/usr/bin/env python3
from setuptools import setup

NAME = 'komodo-python3-dbgp'

setup(
    name=NAME,
    version='9.0.1.dev0',
    description='The ActiveState Komodo DBGP server',

    author="Shane Caraveo, Trent Mick",
    author_email="komodo-feedback@ActiveState.com",
    maintainer='Kevin Velghe',
    maintainer_email='kevin@paretje.be',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],


    url='http://github.com/paretje/komodo-python3-dbgp',
    packages=['dbgp'],
    scripts=['bin/pydbgp',
             'bin/pydbgpproxy'],
    zip_safe=False,
)
