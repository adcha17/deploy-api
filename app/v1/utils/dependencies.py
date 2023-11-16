import os
from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(...)):
    deploy_key = os.environ.get("DEPLOY_KEY")
    if deploy_key is None:
        return {
            "statusCode": 500,
            "message": "Contact with admin, need set deploy key"
        }
    if x_token != deploy_key:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
