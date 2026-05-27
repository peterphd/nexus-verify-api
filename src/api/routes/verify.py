
from fastapi import APIRouter
from pydantic import BaseModel
from src.core.matching import verify

router = APIRouter()

class VerifyRequest(BaseModel):
    nin: str
    name: str
    dob: str

class VerifyResponse(BaseModel):
    result: str
    score: float

@router.post("/v1/verify/demographic", response_model=VerifyResponse)
def verify_demographic(request: VerifyRequest):
    record = {
        "name": "Adeola Bello",
        "dob": "01/01/1990"
    }
    result = verify(
        {"name": request.name, "dob": request.dob},
        record
    )
    return VerifyResponse(result=result["result"], score=result["score"])