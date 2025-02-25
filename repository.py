import os, yaml
from github import Github, GithubException, Auth, Repository

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
ORGANIZATION = os.environ.get("GITHUB_ORG")
REPO_CONFIG = os.environ.get("REPO_CONFIG")
REPO_NAME = "0-test-AWS-12490"
TEST_REPO = "github-workflow-common"

# Get access to the organization using GTIHUB_TOKEN.
auth = Auth.Token(f"{GITHUB_TOKEN}")
g = Github(auth=auth)
g.get_user().login
org = g.get_organization(f"{ORGANIZATION}")

def get_repo(org, repo_name):
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
            print(f"Repository `{repo_name}` does not exists within GitHub {org}")
            return None
        else:
            print(f"Error fetching repository from GitHub {org} - {str(e)}")
            raise e

def create_repository(org, repo_name, description):
    """
    Creates Github repository.
    """
    repo = get_repo(org, repo_name)
    if repo == None:
        print (f"Creating private github repository `{repo_name}`")
        create_repo = org.create_repo(
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
        print (f"Update private github repository `{repo_name}`")
        edit_repo = repo.edit(
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


def get_pull_requests(org, repo_name):
    """
    Get open pull requests for Github repository.
    """
    pr_list=[]
    repo = get_repo(org, repo_name)
    prs = repo.get_pulls(state='open', sort='created', base='master')
    if repo != None:
        print (f"List of open PRs for github repository `{repo_name}`")
        for pr in prs:
            pr_list.append(pr.number)
    return pr_list

def delete_repository(org, repo_name):
    """
    Deletes Github repository.
    """
    repo = get_repo(org, repo_name)
    if repo != None:
        print (f"Deleting github repository `{repo_name}`")
        repo.delete()

def get_open_issues(org, repo_name):
    """
    Get all issues for a Github repository.
    """
    print (f"List of open issues for repository `{repo_name}`")
    if repo != None:
        print (f"Issues for repository `{repo_name}`:")
        open_issues = repo.get_issues(state='open')
        for issue in open_issues:
            print(issue)

def get_labels(org, repo_name):
    """
    Get all labels for a Github repository.
    """
    repo = get_repo(org, repo_name)
    if repo != None:
        print (f"Labels for repository `{repo_name}`:")
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
            f.close()
        except yaml.YAMLError as e:
            print("Invalid YAML", e)

    config = list(repos["repositories"].values())
    for repo in config:
        # print (org, repo["name"], repo["description"])
        create_repository(org, repo["name"], repo["description"])

def repo_decom(repo_config):
    """
    NOTE: This is used for DEMO purposes only.
    To delete repositories based on YAML config.
    For the real repositories this needs to be adjusted.
    """
    with open(f"{repo_config}", 'r') as f:
        try:
            repos = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
        except yaml.YAMLError as e:
            print("Invalid YAML", e)

    config = list(repos["repositories"].values())
    for repo in config:
        delete_repository(org, repo["name"])

# Test functions.
# get_open_issues(org, TEST_REPO)
# get_labels(org, TEST_REPO)
# get_pull_requests(org, TEST_REPO)
# repo_config(REPO_CONFIG)
repo_decom(REPO_CONFIG)
