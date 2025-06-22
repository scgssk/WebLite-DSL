from setuptools import setup, find_packages

setup(
    name='weblite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml', 'shutil', 'argparse'
    ],
    entry_points={
        'console_scripts': [
            'weblite = weblite.cli:main',
        ],
    },
    author='S C G SREE SOORYA KUMAR',
    description='A DSL-based static site generator using YAML.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
)
