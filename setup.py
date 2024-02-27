# setup.py
from setuptools import setup, find_packages

setup(
    name='scientific_calculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tkinter',  # tkinter is included with Python, no need to specify it as a requirement
    ],
    entry_points={
        'console_scripts': [
            'calculator=calculator:main',
        ],
    },
)
