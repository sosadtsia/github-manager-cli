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
        'PyGithub',
        'python-dotenv',
        'PyYAML',
        'rich',
        'requests'
    ],
    author="Sviatoslav Osadtsia",
    author_email="sviatoslav.osadtsia@gmail.com",
    description="A tool to manage GitHub repositories",
    license="GPL-3.0 license",
    url="https://github.com/SLAVNG/github-manager"
)
