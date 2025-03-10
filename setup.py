# setup.py - Defines the configuration for packaging and distributing for the project

from setuptools import setup, find_packages

setup(
    name='github-manager',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'gm=main:main',
        ],
    },
    install_requires=[
        'pylint',
        'PyGithub',
        'python-dotenv',
        'PyYAML',
        'rich',
        'requests',
        'pytest',
        'pytest-cov',
        'pytest-mock',
    ],
)
