from pydantic import BaseModel, Field


class GitSchema(BaseModel):
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
