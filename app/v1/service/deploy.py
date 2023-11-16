import boto3, json, ansible_runner
from fastapi import HTTPException, status
from app.v1.schema.deploy import DeploySchema
from botocore.exceptions import ClientError


def deploy(deploy_schema: DeploySchema):
    path_extravars = '/home/ubuntu/ansible/{}/env/extravars'.format(deploy_schema.project)

    # Set version of deploy
    with open(path_extravars, 'w') as f:
        f.write('version: {}\n'.format(deploy_schema.version))
        f.write('repo_branch: {}\n'.format(deploy_schema.repo_branch))

    # Get env vars
    env_vars = get_env_vars(deploy_schema.arn_secret)
    env_dict = json.loads(env_vars)  # Convert str to dict
    env_file = ''

    # Env style
    if deploy_schema.project == 'subastas':
        for key in env_dict.keys():
            env_var = f'{key}=>{env_dict[key]},\n'
            env_file = env_file + env_var
    else:
        for key in env_dict.keys():
            env_var = f'{key}={env_dict[key]}\n'
            env_file = env_file + env_var

    # Create env file
    env_name = '/tmp/{}'.format(deploy_schema.arn_secret)

    if deploy_schema.project == 'subastas':
        env_file = f'<?php\nreturn [\n{env_file}\n];'

    with open(env_name, 'w') as f:
        f.write(env_file)

    # Run ansible playbook - DEPLOY ON INSTANCES
    private_data_dir = '/home/ubuntu/ansible/{}'.format(deploy_schema.project)
    r = ansible_runner.run(
        private_data_dir=private_data_dir,
        playbook='main.yml',
        tags=deploy_schema.role)  # With tags run specific role

    print("{}: {}".format(r.status, r.rc))

    print("Final status:")
    print(r.stats)

    return {"statusCode": 200, "message": r.status}


def get_env_vars(project: str):
    secret_name = project
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            # print(json.loads(secret))
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
