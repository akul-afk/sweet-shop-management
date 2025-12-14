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
from sqlalchemy import and_

@router.get("/search")
def search_sweets(
    name: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(Sweet)

    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))
    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)
    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)

    return query.all()
@router.put("/{sweet_id}")
def update_sweet(
    sweet_id: int,
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    for field in ["name", "category", "price", "quantity"]:
        if field in payload:
            setattr(sweet, field, payload[field])

    db.commit()
    db.refresh(sweet)
    return sweet
