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

## Sponsors

Please [contact me](https://github.com/sosadtsia) if you want to become a sponsor.

## Contributions

I always want to get feedback and update this project as the community matures and new ideas are implemented and verified over time.

If you are interested in specific topics, please [open an issue](https://github.com/sosadtsia/github-manager.git/issues), or thumb up an issue you want to be covered. If you want to contribute, please submit a pull request.

## License

This project is licensed with [apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Code of Conduct

We are committed to fostering a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand our expectations for respectful participation.

By contributing to this project, you agree to abide by its terms.
