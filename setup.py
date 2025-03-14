from setuptools import setup, find_packages

setup(
    name='gh-repository-manager',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'grm=main:main',
        ],
    },
    install_requires=[
        'PyGithub',
        'python-dotenv',
        'PyYAML',
        'rich',
        'requests'
    ],
    author="Slav",
    description="A tool to manage GitHub repositories",
    url="https://github.com/SLAVNG/github-manager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
