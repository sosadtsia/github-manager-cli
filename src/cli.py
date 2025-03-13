import argparse
import os
import yaml
from rich.text import Text
from dotenv import load_dotenv
from github import Github, GithubException, Auth
from repository import (
    configure_repository,
    decommission_repository,
    create_repository,
    delete_repository
)

from display import (
    display_result,
    display_list,
    display_empty
)

from notifications.slack import send_slack_notification
from notifications.discord import send_discord_notification

# Load environment variables from .env file
load_dotenv()

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_ORG = os.environ.get("GITHUB_ORG")

# Get access to the organization using GITHUB_TOKEN.
auth = Auth.Token(f"{GITHUB_TOKEN}")
g = Github(auth=auth)
org = g.get_organization(f"{GITHUB_ORG}")

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def run_cli():
    parser = argparse.ArgumentParser(description="GitHub Repository Manager CLI")
    parser.add_argument("action", choices=[
        "create",
        "delete",
    ], help="Action to perform")

    # Config argument
    parser.add_argument("--config", help="Path to YAML config file", required=True)

    args = parser.parse_args()

    config = load_config(args.config)
    repos = config.get('repositories', {})
    description = config.get('description')

    def send_notification(action, details, status="success"):
        if SLACK_WEBHOOK_URL:
            send_slack_notification(action, details, status)
        if DISCORD_WEBHOOK_URL:
            send_discord_notification(action, details, status)

    try:
        # Handle repository creation based on YAML config
        for repo_name, repo_config in repos.items():
            if args.action == "create":
                create_repository(repo_name, description=repo_config.get('description'))
                send_notification(
                    "Repository Created",
                    {
                        "Repository": repo_name,
                        "Description": repo_config.get('description')
                    },
                    "success"
                )
                display_result(
                    Text.assemble(
                        "GitHub repository created: ",
                        (repo_name, "bold green")
                    ),
                    "success"
                )

            # Handle repository deletion based on YAML config
            elif args.action == "delete":
                delete_repository(repo_name)
                send_notification(
                    "Repository Deleted",
                    {
                        "Repository": repo_name
                    },
                    "warning"
                )
                display_result(
                    Text.assemble(
                        "GitHub repository deleted: ",
                        (repo_name, "bold red")
                    ),
                    "warning"
                )

    except Exception as e:
        error_message = str(e)
        send_notification(
            "Error Occurred",
            {
                "Action": args.action,
                "Error": error_message
            },
            "error"
        )
        display_result(
            Text.assemble(
                "Error: ",
                (error_message, "bold red")
            ),
            "error"
        )

if __name__ == "__main__":
    run_cli()
