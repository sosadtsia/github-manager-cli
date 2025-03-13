import argparse
import os
import yaml
from rich.text import Text
from repository import (
    configure_repository,
    decommission_repository
)

from display import (
    display_result,
    display_list,
    display_empty
)

from notifications.slack import send_slack_notification
from notifications.discord import send_discord_notification

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
    repo = config.get('repo')
    description = config.get('description')

    def send_notification(action, details, status="success"):
        if SLACK_WEBHOOK_URL:
            send_slack_notification(action, details, status)
        if DISCORD_WEBHOOK_URL:
            send_discord_notification(action, details, status)

    try:
        if args.action == "create" and args.config:
            configure_repository(args.config)
            send_notification(
                "Configuration Applied",
                {
                    "Config File": args.config
                },
                "success"
            )
            display_result(
                Text.assemble(
                    "Configuration applied from: ",
                    (args.config, "bold green")
                ),
                "success"
            )

        elif args.action == "delete" and args.config:
            decommission_repository(args.config)
            send_notification(
                "Repository Decommissioned",
                {
                    "Config File": args.config
                },
                "warning"
            )
            display_result(
                Text.assemble(
                    "Decommissioning completed from: ",
                    (args.config, "bold yellow")
                ),
                "warning"
            )

        # Handle repository creation based on YAML config
        if repo and description:
            create_repository(repo, description=description)
            send_notification(
                "Repository Created",
                {
                    "Repository": repo,
                    "Description": description
                },
                "success"
            )
            display_result(
                Text.assemble(
                    "Repository created: ",
                    (repo, "bold green")
                ),
                "success"
            )

        # Handle repository deletion based on YAML config
        if repo:
            delete_repository(repo)
            send_notification(
                "Repository Deleted",
                {
                    "Repository": repo
                },
                "warning"
            )
            display_result(
                Text.assemble(
                    "Repository deleted: ",
                    (repo, "bold red")
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
