from setuptools import setup, find_packages

setup(
    name='package',

    version = '0.1',

    description='demo Python package for DIY-Python',
    url='https://github.com/Memcys/DIY-Python/package/',
    
    author='Memcys',

    # Following https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages
    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)