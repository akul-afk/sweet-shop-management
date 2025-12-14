from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register():
    return {"message": "user registered"}
