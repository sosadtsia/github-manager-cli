import argparse
from rich.text import Text
from repository import (
    create_repository,
    delete_repository,
    get_open_issues,
    get_labels, get_pull_requests,
    repo_config,
    repo_decom
)

from display import (
    display_result,
    display_list,
    display_empty
)

from notifications import create_notification

def main():
    parser = argparse.ArgumentParser(description="GitHub Repository Manager CLI")
    parser.add_argument("action", choices=[
        "create",
        "delete",
        "issues",
        "labels",
        "pulls",
        "config",
        "decom",
        "new-issue"
    ], help="Action to perform")

    # Repository arguments
    parser.add_argument("--repo", help="The name of the repository")
    parser.add_argument("--description", help="The description of the repository")
    parser.add_argument("--config", help="Path to YAML config file")

    # Issue arguments
    parser.add_argument("--title", help="Issue title")
    parser.add_argument("--body", help="Issue body")
    parser.add_argument("--labels", help="Comma-separated list of labels", default="")

    # Issue filtering arguments
    parser.add_argument("--state", choices=["open", "closed", "all"], default="all", help="Filter issues by state")
    parser.add_argument("--assignee", help="Filter by assignee (use 'none' for unassigned)")

    args = parser.parse_args()

    try:
        if args.action == "create" and args.repo and args.description:
            create_repository(args.repo, args.description)
            create_notification(
                "Repository Created",
                {
                    "Repository": args.repo,
                    "Description": args.description
                },
                "success"
            )
            display_result(
                Text.assemble(
                    "Repository created: ",
                    (args.repo, "bold green")
                ),
                "success"
            )

        elif args.action == "delete" and args.repo:
            delete_repository(args.repo)
            create_notification(
                "Repository Deleted",
                {
                    "Repository": args.repo
                },
                "warning"
            )
            display_result(
                Text.assemble(
                    "Repository deleted: ",
                    (args.repo, "bold red")
                ),
                "warning"
            )

        elif args.action == "issues" and args.repo:
            issues = get_issues(
                args.repo,
                state=args.state,
                labels=args.labels,
                assignee=args.assignee
            )
            create_notification(
                "Issues Retrieved",
                {
                    "Repository": args.repo,
                    "State": args.state,
                    "Labels": args.labels if args.labels else "all",
                    "Assignee": args.assignee if args.assignee else "all",
                    "Count": len(issues)
                },
                "info"
            )
            display_result(
                Text.assemble(
                    "Open issues for ",
                    (args.repo, "bold blue"),
                    f"\nState: {args.state}",
                    f"\nLabels: {args.labels if args.labels else 'all'}",
                    f"\nAssignee: {args.assignee if args.assignee else 'all'}"
                ),
                "info"
            )
            if issues:
                display_list(
                    f"Issues for {args.repo}",
                    issues,
                    ["Number", "Title", "State", "Created", "Labels", "Assignee"]
                )
            else:
                display_empty("No issues found matching the criteria")

        elif args.action == "labels" and args.repo:
            labels = get_labels(args.repo)
            create_notification(
                "Labels Retrieved",
                {
                    "Repository": args.repo,
                    "Count": len(labels) if labels else 0
                },
                "info"
            )
            display_result(f"Labels for {args.repo}:", "info")
            if labels:
                display_list(
                    f"Labels for {args.repo}",
                    labels,
                    ["Name", "Description", "Color"]
                )
            else:
                display_empty("No labels found")

        elif args.action == "pulls" and args.repo:
            pulls = get_pull_requests(args.repo)
            create_notification(
                "Pull Requests Retrieved",
                {
                    "Repository": args.repo,
                    "Count": len(pulls) if pulls else 0
                },
                "info"
            )
            display_result(f"Pull requests for {args.repo}:", "info")
            if pulls:
                display_list(
                    f"Pull Requests for {args.repo}",
                    pulls,
                    ["Number", "Title", "State", "Created At"]
                )
            else:
                display_empty("No pull requests found")

        elif args.action == "config" and args.config:
            repo_config(args.config)
            create_notification(
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

        elif args.action == "decom" and args.config:
            repo_decom(args.config)
            create_notification(
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

        elif args.action == "new-issue" and args.repo and args.title:
            # Convert comma-separated labels to list
            labels = [label.strip() for label in args.labels.split(",")] if args.labels else []
            issue = create_issue(args.repo, args.title, args.body, labels)
            create_notification(
                "Issue Created",
                {
                    "Repository": args.repo,
                    "Issue": f"#{issue.number}",
                    "Title": issue.title,
                    "Labels": ", ".join(labels) if labels else "None"
                },
                "success"
            )
            display_result(
                Text.assemble(
                    "Issue created: ",
                    (f"#{issue.number}", "bold blue"),
                    " - ",
                    (issue.title, "bold green")
                ),
                "success"
            )

        else:
            parser.print_help()

    except Exception as e:
        error_message = str(e)
        create_notification(
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
    main()
