import json, typer, requests, os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()
app = typer.Typer()


class Project(Enum):
    services = "services"
    subastas = "subastas"


@app.command()
def checkout(project: Project, repo_branch: str):
    """
    If have an error, please make sure you configure env file first.
    """
    headers = {"x-token": os.environ.get("DEPLOY_KEY")}
    checkout = {"project": project.value, "repo_branch": repo_branch, "role": "git_checkout"}
    response = requests.post(f'{os.environ.get("URL_API")}/checkout', data=json.dumps(checkout), headers=headers)
    print(response.text)


@app.command()
def pull(project: Project, repo_branch: str):
    """
    If have an error, please make sure you configure env file first.
    """
    headers = {"x-token": os.environ.get("DEPLOY_KEY")}
    pull = {"project": project.value, "repo_branch": repo_branch, "role": "git_pull"}
    response = requests.post(f'{os.environ.get("URL_API")}/pull', data=json.dumps(pull), headers=headers)

    print(response.text)


@app.command()
def status(project: Project):
    """
    If have an error, please make sure you configure env file first.
    """
    headers = {"x-token": os.environ.get("DEPLOY_KEY")}
    status = {"project": project.value, "role": "git_status"}
    response = requests.post(f'{os.environ.get("URL_API")}/status', data=json.dumps(status), headers=headers)

    print(response.json()["stdout"])


if __name__ == "__main__":
    app()
