import boto3, json, ansible_runner
from fastapi import HTTPException, status
from app.v1.schema.git import GitSchema


def pull(git_schema: GitSchema):
    path_extravars = '/home/ubuntu/ansible/{}/env/extravars'.format(git_schema.project)

    # Save extravars
    lines = []
    with open(path_extravars, 'r') as f:
        lines = f.readlines()

    word = 'repo_branch'
    for line in lines:
        if line.find(word)!=-1:
            lines.remove(line)
            lines.append(f'repo_branch: {git_schema.repo_branch}\n')

    with open(path_extravars, 'w') as f:
        for line in lines:
            f.write(line)

    # Run ansible playbook - DEPLOY ON INSTANCES
    private_data_dir = '/home/ubuntu/ansible/{}'.format(git_schema.project)
    r = ansible_runner.run(
        private_data_dir=private_data_dir,
        playbook='main.yml',
        tags=git_schema.role)  # With tags run specific role

    print("{}: {}".format(r.status, r.rc))

    print("Final status:")
    print(r.stats)

    return {"statusCode": 200, "message": r.status}
