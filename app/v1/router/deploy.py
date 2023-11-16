from fastapi import APIRouter
from fastapi import Depends
from fastapi import Body

from app.v1.utils.dependencies import get_token_header
from app.v1.schema.deploy import DeploySchema
from app.v1.schema.git import GitSchema
from app.v1.schema.git_status import GitStatusSchema
from app.v1.service.deploy import deploy as deploy_service
from app.v1.service.checkout import checkout as checkout_service
from app.v1.service.pull import pull as pull_service
from app.v1.service.status import status as status_service

router = APIRouter(prefix="/api/v1")


@router.post(
    "/",
    tags=["Deploy"],
    # status_code=status.HTTP_201_CREATED,
    # response_model=user_schema.User,
    dependencies=[Depends(get_token_header)],
    summary="Deploy new version"
)
async def deploy(deploy: DeploySchema = Body(...)):
    """
    ## Start deploy of new version

    ### Args
    The app can recive next fields into a JSON
    - arn_secret: arn aws secrets manager
    - project: Project to deploy
    - repo_branch: Project branch
    - role: Ansible role
    - version: A valid version string

    ### Returns
    - statusCode: A status code of process
    - message: A status of process
    """
    return deploy_service(deploy)


@router.post(
    "/checkout",
    tags=["Deploy"],
    # status_code=status.HTTP_201_CREATED,
    # response_model=user_schema.User,
    dependencies=[Depends(get_token_header)],
    summary="Move project to specific branch"
)
async def checkout(checkout: GitSchema = Body(...)):
    """
    ## Move project to specific branch

    ### Args
    The app can recive next fields into a JSON
    - project: Project to deploy
    - repo_branch: Project branch
    - role: Ansible role

    ### Returns
    - statusCode: A status code of process
    - message: A status of process
    """
    return checkout_service(checkout)


@router.post(
    "/pull",
    tags=["Deploy"],
    # status_code=status.HTTP_201_CREATED,
    # response_model=user_schema.User,
    dependencies=[Depends(get_token_header)],
    summary="Move project to specific branch"
)
async def pull(pull: GitSchema = Body(...)):
    """
    ## Update branch

    ### Args
    The app can recive next fields into a JSON
    - project: Project to deploy
    - repo_branch: Project branch
    - role: Ansible role

    ### Returns
    - statusCode: A status code of process
    - message: A status of process
    """
    return pull_service(pull)


@router.post(
    "/status",
    tags=["Deploy"],
    # status_code=status.HTTP_201_CREATED,
    # response_model=user_schema.User,
    dependencies=[Depends(get_token_header)],
    summary="Get status of repository"
)
async def status(status: GitStatusSchema):
    """
    ## Get status of repository

    ### Args
    The app can recive next fields into a JSON
    - project: Project to deploy
    - role: Ansible role

    ### Returns
    - statusCode: A status code of process
    - message: A status of process
    """
    return status_service(status)
