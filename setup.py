import setuptools
from setuptools import setup

setup(
    name='pyAnIML',
    version='0.0.2',
    description='Handling of AnIML files',
    url='https://github.com/FAIRChemistry/pyAnIML',
    author='Range, Jan',
    author_email='jan.range@simtech.uni-stuttgart.de',
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=[
        'xsdata',
        'pydantic'
    ]
)
