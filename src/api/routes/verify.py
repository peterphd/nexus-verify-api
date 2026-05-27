from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
from src.core.matching import verify

router = APIRouter()

# Fake database — in Project 2 this becomes a real Postgres table
RECORDS = {
    "12345678901": {"name": "Adeola Bello", "dob": "01/01/1990"},
    "98765432101": {"name": "Chukwuma Okafor", "dob": "15/03/1985"},
    "11122233344": {"name": "Fatima Aliyu", "dob": "22/07/1995"},
}

class VerifyRequest(BaseModel):
    nin: str
    name: str
    dob: str

    @field_validator("nin")
    @classmethod
    def nin_must_be_valid(cls, v):
        if not v.isdigit():
            raise ValueError("NIN must contain digits only")
        if len(v) != 11:
            raise ValueError("NIN must be exactly 11 digits")
        return v

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip()

class VerifyResponse(BaseModel):
    result: str
    score: float
    message: str

@router.post("/v1/verify/demographic", response_model=VerifyResponse)
def verify_demographic(request: VerifyRequest):
    record = RECORDS.get(request.nin)

    if not record:
        raise HTTPException(
            status_code=404,
            detail=f"NIN {request.nin} not found"
        )

    result = verify(
        {"name": request.name, "dob": request.dob},
        record
    )

    messages = {
        "MATCH": "Identity verified successfully",
        "PARTIAL": "Partial match — possible data entry error",
        "NO_MATCH": "Identity could not be verified"
    }

    return VerifyResponse(
        result=result["result"],
        score=result["score"],
        message=messages[result["result"]]
    )
