import os
import yaml
from dotenv import load_dotenv
from github import Github, GithubException, Auth

# Load environment variables from .env file
load_dotenv()

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_ORG = os.environ.get("GITHUB_ORG")

# Get access to the organization using GITHUB_TOKEN.
auth = Auth.Token(f"{GITHUB_TOKEN}")
g = Github(auth=auth)
org = g.get_organization(f"{GITHUB_ORG}")

def get_repo(repo_name):
    """
    Fetches a repo from GitHub organization.
    """
    try:
        repo = org.get_repo(repo_name)
        if repo.name:
            print(f"Repository `{repo_name}` exists within GitHub {org}")
            return repo
    except GithubException as e:
        if e.status == 404:
            print(f"Repository `{repo_name}` does not exist within GitHub {org}")
            return None
        else:
            print(f"Error fetching repository from GitHub {org} - {str(e)}")
            raise e

def create_repository(repo_name, description):
    """
    Creates GitHub repository.
    """
    repo = get_repo(repo_name)
    if repo is None:
        print(f"Creating private GitHub repository `{repo_name}`")
        org.create_repo(
            allow_auto_merge=False,
            allow_merge_commit=True,
            allow_rebase_merge=False,
            allow_squash_merge=False,
            allow_update_branch=False,
            delete_branch_on_merge=True,
            description=description,
            has_issues=True,
            has_wiki=True,
            has_projects=False,
            name=repo_name,
            private=True,
            visibility="internal"
        )
    else:
        print(f"Update private GitHub repository `{repo_name}`")
        repo.edit(
            allow_auto_merge=False,
            allow_merge_commit=True,
            allow_rebase_merge=False,
            allow_squash_merge=False,
            allow_update_branch=False,
            delete_branch_on_merge=True,
            description=description,
            has_issues=True,
            has_wiki=False,
            has_projects=False,
            name=repo_name,
            private=True,
            visibility="internal"
        )

def get_pull_requests(repo_name):
    """
    Get open pull requests for GitHub repository.
    """
    pr_list = []
    repo = get_repo(repo_name)
    if repo:
        prs = repo.get_pulls(state='open', sort='created', base='master')
        print(f"List of open PRs for GitHub repository `{repo_name}`")
        for pr in prs:
            pr_list.append(pr.number)
    return pr_list

def delete_repository(repo_name):
    """
    Deletes GitHub repository.
    """
    repo = get_repo(repo_name)
    if repo:
        print(f"Deleting GitHub repository `{repo_name}`")
        repo.delete()

def get_open_issues(repo_name):
    """
    Get all issues for a GitHub repository.
    """
    repo = get_repo(repo_name)
    if repo:
        print(f"List of open issues for repository `{repo_name}`")
        open_issues = repo.get_issues(state='open')
        for issue in open_issues:
            print(issue)

def get_labels(repo_name):
    """
    Get all labels for a GitHub repository.
    """
    repo = get_repo(repo_name)
    if repo:
        print(f"Labels for repository `{repo_name}`")
        labels = repo.get_labels()
        for label in labels:
            print(label)

def repo_config(repo_config):
    """
    Used to create repositories based on YAML config.
    """
    with open(f"{repo_config}", 'r') as f:
        try:
            repos = yaml.load(f, Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            print("Invalid YAML", e)
            return

    config = list(repos["repositories"].values())
    for repo in config:
        create_repository(repo["name"], repo["description"])

def repo_decom(repo_config):
    """
    NOTE: This is used for DEMO purposes only.
    To delete repositories based on YAML config.
    For the real repositories this needs to be adjusted.
    """
    with open(f"{repo_config}", 'r') as f:
        try:
            repos = yaml.load(f, Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            print("Invalid YAML", e)
            return

    config = list(repos["repositories"].values())
    for repo in config:
        delete_repository(repo["name"])
