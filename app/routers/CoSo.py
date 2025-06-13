from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.CoSo import CoSoCreate, CoSoRead, CoSoUpdate
from app.crud import CoSo as crud
from app.database import get_session

router = APIRouter(
    prefix="/co_so",
    tags=["CoSo"]
)

@router.post("/", response_model=CoSoRead)
def create_co_so(data: CoSoCreate, db: Session = Depends(get_session)):
    return crud.create_co_so(db, data)

@router.get("/", response_model=list[CoSoRead])
def get_all_co_so(db: Session = Depends(get_session)):
    return crud.get_all_co_so(db)

@router.put("/{co_so_id}", response_model=CoSoRead)
def update_co_so(co_so_id: int, data: CoSoUpdate, db: Session = Depends(get_session)):
    co_so = crud.update_co_so(db, co_so_id, data)
    if not co_so:
        raise HTTPException(status_code=404, detail="Cơ sở không tồn tại")
    return co_so

@router.delete("/{co_so_id}")
def delete_co_so(co_so_id: int, db: Session = Depends(get_session)):
    result = crud.delete_co_so(db, co_so_id)
    if not result:
        raise HTTPException(status_code=404, detail="Cơ sở không tồn tại")
    return {"message": "Xoá thành công"}
