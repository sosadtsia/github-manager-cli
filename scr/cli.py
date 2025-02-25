import argparse
from repository import create_repository, delete_repository, get_open_issues, get_labels, get_pull_requests, repo_config, repo_decom

def main():
    parser = argparse.ArgumentParser(description="GitHub Repository Manager CLI")
    parser.add_argument("action", choices=["create", "delete", "issues", "labels", "pulls", "config", "decom"], help="Action to perform")
    parser.add_argument("--repo", help="Repository name")
    parser.add_argument("--description", help="Repository description")
    parser.add_argument("--config", help="Path to YAML config file")

    args = parser.parse_args()

    if args.action == "create" and args.repo and args.description:
        create_repository(args.repo, args.description)
    elif args.action == "delete" and args.repo:
        delete_repository(args.repo)
    elif args.action == "issues" and args.repo:
        get_open_issues(args.repo)
    elif args.action == "labels" and args.repo:
        get_labels(args.repo)
    elif args.action == "pulls" and args.repo:
        get_pull_requests(args.repo)
    elif args.action == "config" and args.config:
        repo_config(args.config)
    elif args.action == "decom" and args.config:
        repo_decom(args.config)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
