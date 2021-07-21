from subprocess import call
from json import load


def getGHIssues(
    repo: str = "",
    limit: int = 10000,
    state: str = "all",
    filename: str = "issues.json",
) -> int:
    if repo == "":
        command: str = f'gh issue list --json "closedAt,createdAt,id,number,state" --limit {limit} --state {state} --search "sort:created-asc"> {filename}'
    else:
        command: str = f'gh issue list --repo {repo} --json "closedAt,createdAt,id,number,state" --limit {limit} --state {state} --search "sort:created-asc" > {filename}'

    return call(command, shell=True)


def loadJSON(filename: str = "issues.json") -> dict:
    with open(file=filename, mode="r") as json:
        return load(json)


getGHIssues(repo="numpy/numpy", limit=10)
