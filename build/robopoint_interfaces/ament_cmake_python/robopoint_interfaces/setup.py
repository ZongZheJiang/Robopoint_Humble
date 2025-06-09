from setuptools import find_packages
from setuptools import setup

setup(
    name='robopoint_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('robopoint_interfaces', 'robopoint_interfaces.*')),
)
