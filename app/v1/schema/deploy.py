from pydantic import BaseModel, Field


class DeploySchema(BaseModel):
    arn_secret: str = Field(
        ...,                # indicates that this field is required
        example="arn:aws:secretsmanager:us-east-x:xxxxxxx:secret:xxxxxx-xxxxxxx"
    )
    project: str = Field(
        ...,
        example="xxxxxxxxxxx"
    )
    repo_branch: str = Field(
        ...,
        example="xxxxxxxxxxx"
    )
    role: str = Field(
        ...,
        example="xxxxxxxxxxx"
    )
    version: str = Field(
        ...,
        example="v1.0"
    )
