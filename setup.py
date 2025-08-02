from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
        name='zigzag',
        ext_modules=cythonize("zigzag/core.pyx"),
        zip_safe=False,
        include_dirs=[numpy.get_include()]
        )
