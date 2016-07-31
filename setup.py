from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: MacOS',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(
    name             = 'pyOnenet',
    version          = '1.1.1',
    author           = 'Jack Zhong',
    author_email     = 'jzopen@yeah.net,
    packages         = ['pyOnenet'],
    py_modules       = ['ez_setup'],
    url              = 'https://github.com/ardypro/pyOnenet',
    license          = 'MIT',
    keywords         = 'Adafruit IO, Onenet',
    classifiers      = classifiers,
    description      = 'Client library for onenet (open.iot.10086.cn).',
    long_description = open('README.md').read(),
    install_requires = ["requests", "paho-mqtt"]
)
