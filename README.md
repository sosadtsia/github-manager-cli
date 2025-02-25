# GitHub Manager

## Overview
GitHub Manager is a Python application designed to help users manage their GitHub repositories, issues, and pull requests efficiently. It provides functionalities for handling labels and other repository-related tasks.

## Features
- Manage labels for GitHub repositories
- Core functionalities for managing repositories, issues, and pull requests
- Utility functions for common tasks

## Installation
To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage
To use the GitHub Manager, you can run the main script in the `src` directory. Make sure to configure your label settings in the `config\labeler.yaml` file.

```
python src/cli.py create --repo my-repo --description "My new repository"
python src/cli.py delete --repo my-repo
python src/cli.py issues --repo my-repo
python src/cli.py labels --repo my-repo
python src/cli.py pulls --repo my-repo
python src/cli.py config --config path/to/config.yaml
python src/cli.py decom --config path/to/config.yaml
```

## Contribution
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.


