#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
USB Energetics Spy
−−−−−−−−−−−−

    copyright : Copyright 2020 Antoine Kristanek and contributors, see AUTHORS.
    license : GNU GPL v3.
'''

import sys
import os
from setuptools import setup, find_packages
import USB_Energetics_Spy

here = os.path.abspath(os.path.dirname( __file__ ))
README = ' '
CHANGES = ' '
try :
    README = open (os.path.join(here, 'README.rst')).read()
    #CHANGES = open (os.path.join(here, 'CHANGES.rst')).read()
except :
    pass
REQUIREMENTS = [
'wxmplot',
]

setup(
    name='USB_Energetics_Spy' ,
    version=USB_Energetics_Spy.__version__,
    url='https://github.com/Beldramma/USB_Energetics_Project_Polytech_2020' ,
    license='GNU GPL v3' ,
    description='Printing measurement curves from .txt files with a GUI' ,
    long_description=README,
    author='Antoine Kristanek',
    author_email='geekophilie@gmail.com',
    maintainer='Lionel Darras',
    maintainer_email='Lionel.Darras@obs.ujf−grenoble.fr',
    package_data={'data': ['*.txt']},
    include_package_data=True,
    #data_files = [('data',['*.txt'])],
    classifiers=[
    'Development Status :: 1 − Beta',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3 ',
    'Topic :: Utilities',
    'Topic : : Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(),
    zip_safe=False,
    install_requires=REQUIREMENTS,
)
