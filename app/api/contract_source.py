import os
import boto3
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

s3_client = boto3.client(
    's3',
    region_name=os.getenv('S3_REGION'),
    aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('S3_SECRET_KEY')
)

@router.get("/contract_source")
async def get_contract_source(name: str):
    try:
        response = s3_client.get_object(
            Bucket='ai-contracts',
            Key=name
        )
        return FileResponse(
            response['Body'].read(),
            media_type='application/pdf',
            headers={"Content-Disposition": "inline"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))