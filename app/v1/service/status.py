import boto3, json, ansible_runner
from fastapi import HTTPException
from app.v1.schema.git_status import GitStatusSchema


def status(git_status: GitStatusSchema):

    # Run ansible playbook - DEPLOY ON INSTANCES
    private_data_dir = '/home/ubuntu/ansible/{}'.format(git_status.project)
    r = ansible_runner.run(
        private_data_dir=private_data_dir,
        playbook='main.yml',
        tags=git_status.role)  # With tags run specific role

    events = list(r.events)

    return {
        "statusCode": 200,
        "message": r.status,
        "stdout": events[-2]["event_data"]["res"]["stdout"]}
