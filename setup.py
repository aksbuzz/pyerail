# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:

    readme = f.read()

with open('LICENSE') as f:

    license = f.read()

setup(

    name='pyerail',

    version='0.2.1',

    description='Python wrapper for eRail API.',

    long_description=readme,

    author='Akshay',

    author_email='akshayjr69@gmail.com',

    url='https://github.com/aksbuzz/PyeRail',

    license=license,

    packages=find_packages(exclude=('tests', 'docs'))
)