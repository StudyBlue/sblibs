# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sblibs.version import __version__

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='sblibs',
    version=__version__,
    description='sblibs package',
    long_description=readme,
    author='Fred Vassard',
    author_email='azafred@gmail.com',
    url='https://github.com/azafred/sblibs',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=required,
    tests_require=['nose', 'testfixtures', 'mock'],
    test_suite="nose.collector",
    entry_points={
        'console_scripts': [
            'sblibs = sblibs.main:main'
        ]
    },
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Operating System :: MacOS'
    ]
)

