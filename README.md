# GitHub Manager

## Overview
GitHub Manager is a Python application designed to help users manage their GitHub repositories, issues, and pull requests efficiently. It provides functionalities for handling labels and other repository-related tasks.

## Features
- Manage labels for GitHub repositories
- Core functionalities for managing repositories, issues, and pull requests
- Utility functions for common tasks
- Notifications via Slack and Discord

## Installation
To install the required dependencies, run the following command:

```sh
pip install -r requirements.txt
```

To install the `gm` CLI tool, run the following command:

```sh
pip install -e .
```

## Configuration
Create a `.env` file in the root directory of the project and add the following environment variables:

```env
GITHUB_TOKEN=your_github_token
GITHUB_ORG=your_github_org
DISCORD_WEBHOOK_URL=your_discord_webhook
SLACK_WEBHOOK_URL=your_slack_webhook
```

## Usage
To use the GitHub Manager, you can run the `gm` command. Make sure to configure your label settings in the `config/labeler.yaml` file.

```sh
gm create --repo my-repo --description "My new repository"
gm delete --repo my-repo
gm issues --repo my-repo
gm labels --repo my-repo
gm pulls --repo my-repo
gm config --config path/to/config.yaml
gm decom --config path/to/config.yaml
gm new-issue --repo my-repo --title "Issue title" --body "Issue body" --labels "bug,enhancement"
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
