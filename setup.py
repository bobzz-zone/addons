# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='addons',
    version=version,
    description='App for Trimatari',
    author='Bobzz Zone',
    author_email='bobzz.zone@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
