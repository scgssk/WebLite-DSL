# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

this_dir = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(this_dir, "README.md")

setup(
    name='weblite',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml>=5.3', 
        'watchdog>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'weblite = weblite.cli:main',
        ],
    },
    author='S C G Sree Soorya Kumar',
    description='A DSL-based static site generator using YAML.',
    long_description=open(readme_path, encoding='utf-8').read() if os.path.exists(readme_path) else '',
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
