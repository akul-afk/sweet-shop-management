from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.sweet import Sweet
from app.core.deps import get_current_user

router = APIRouter(prefix="/api/sweets", tags=["sweets"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_sweet(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    sweet = Sweet(
        name=payload["name"],
        category=payload["category"],
        price=payload["price"],
        quantity=payload["quantity"],
    )
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet


@router.get("")
def list_sweets(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Sweet).all()
