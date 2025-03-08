import argparse
from repository import create_repository, delete_repository, get_open_issues, get_labels, get_pull_requests, repo_config, repo_decom
from pycowsay import cow

def display_result(message):
    print(cow.milk(message))

def main():
    parser = argparse.ArgumentParser(description="GitHub Repository Manager CLI")
    parser.add_argument("action", choices=["create", "delete", "issues", "labels", "pulls", "config", "decom"], help="Action to perform")
    parser.add_argument("--repo", help="The name of the repository")
    parser.add_argument("--description", help="The description of the repository")
    parser.add_argument("--config", help="Path to YAML config file")

    args = parser.parse_args()

    if args.action == "create" and args.repo and args.description:
        result = create_repository(args.repo, args.description)
        display_result(f"Repository created: {args.repo}")
    elif args.action == "delete" and args.repo:
        result = delete_repository(args.repo)
        display_result(f"Repository deleted: {args.repo}")
    elif args.action == "issues" and args.repo:
        issues = get_open_issues(args.repo)
        display_result(f"Open issues for {args.repo}:\n{issues}")
    elif args.action == "labels" and args.repo:
        labels = get_labels(args.repo)
        display_result(f"Labels for {args.repo}:\n{labels}")
    elif args.action == "pulls" and args.repo:
        pulls = get_pull_requests(args.repo)
        display_result(f"Pull requests for {args.repo}:\n{pulls}")
    elif args.action == "config" and args.config:
        result = repo_config(args.config)
        display_result(f"Configuration applied from: {args.config}")
    elif args.action == "decom" and args.config:
        result = repo_decom(args.config)
        display_result(f"Decommissioning completed from: {args.config}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
