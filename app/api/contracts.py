from fastapi import APIRouter, HTTPException
from typing import List
from ..models.contract import Contract
from ..database import Database

router = APIRouter()
db = Database()

@router.get("/contracts", response_model=List[Contract])
async def get_contracts():
    try:
        contracts = list(db.collection.find(
            {}, 
            {"filename": 1, "intellectual_properties": 1}
        ).sort("filename", 1))
        return contracts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))