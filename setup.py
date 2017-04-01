#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup
import pkg_resources
from distutils.extension import Extension
from distutils.command.build_ext import build_ext as build_ext

NAME = 'pandas-msgpack'

def is_platform_windows():
    return sys.platform == 'win32' or sys.platform == 'cygwin'

def is_platform_linux():
    return sys.platform == 'linux2'

def is_platform_mac():
    return sys.platform == 'darwin'

# versioning
import versioneer
cmdclass = versioneer.get_cmdclass()

try:
    import Cython
    from Cython.Build import cythonize
except ImportError:
    raise ImportError("cython is required for building")

# args to ignore warnings
if is_platform_windows():
    extra_compile_args=[]
else:
    extra_compile_args=['-Wno-unused-function']


if sys.byteorder == 'big':
    macros = [('__BIG_ENDIAN__', '1')]
else:
    macros = [('__LITTLE_ENDIAN__', '1')]

extensions = []
packer_ext = Extension('pandas_msgpack.msgpack._packer',
                        depends=['pandas_msgpack/includes/pack.h',
                                 'pandas_msgpack/includes/pack_template.h'],
                        sources = ['pandas_msgpack/msgpack/_packer.pyx'],
                        language='c++',
                        include_dirs=['pandas_msgack/includes'],
                        define_macros=macros,
                        extra_compile_args=extra_compile_args)
unpacker_ext = Extension('pandas_msgpack.msgpack._unpacker',
                        depends=['pandas_msgpack/includes/unpack.h',
                                 'pandas_msgpack/includes/unpack_define.h',
                                 'pandas_msgpack/includes/unpack_template.h'],
                        sources = ['pandas_msgpack/msgpack/_unpacker.pyx'],
                         language='c++',
                        include_dirs=['pandas_msgpack/includes'],
                        define_macros=macros,
                        extra_compile_args=extra_compile_args)
extensions.append(packer_ext)
extensions.append(unpacker_ext)

#----------------------------------------------------------------------
# util
# extension for pseudo-safely moving bytes into mutable buffers
_move_ext = Extension('pandas_msgpack._move',
                      depends=[],
                      sources=['pandas_msgpack/move.c'])
extensions.append(_move_ext)


def readme():
    with open('README.rst') as f:
        return f.read()

INSTALL_REQUIRES = (
    ['pandas']
)

setup(
    name=NAME,
    version=versioneer.get_version(),
    cmdclass=cmdclass,
    description="Pandas interface to msgpack",
    long_description=readme(),
    license='BSD License',
    author='The PyData Development Team',
    author_email='pydata@googlegroups.com',
    url='https://github.com/pydata/pandas-msgpack',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
    ],
    ext_modules=cythonize(extensions),
    keywords='data',
    install_requires=INSTALL_REQUIRES,
    packages=['pandas_msgpack',
              'pandas_msgpack.includes',
              'pandas_msgpack.msgpack',
              'pandas_msgpack.tests'],
    test_suite='tests',
)
