from pydantic import BaseModel, Field


class GitStatusSchema(BaseModel):
    project: str = Field(
        ...,
        example="xxxxxxxxxxx"
    )
    role: str = Field(
        ...,
        example="xxxxxxxxxxx"
    )
