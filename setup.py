from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy

setup(
    name='zigzag',
    packages=find_packages(),  # zigzag 하위 디렉토리를 모두 패키지로 인식해 줌
    ext_modules=cythonize("zigzag/core.pyx"),
    include_dirs=[numpy.get_include()],
    include_package_data=True,  # MANIFEST.in 등에서 지정한 추가 파일 포함
    zip_safe=False,
)
