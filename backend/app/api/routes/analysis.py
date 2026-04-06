from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.analysis import Analysis
from app.schemas.analysis import AnalyzeRequest, AnalysisResult
from app.services import inference

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult, status_code=status.HTTP_201_CREATED)
def analyze(
    body: AnalyzeRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = inference.run(body.text)
    record = Analysis(user_id=current_user.id, input_text=body.text, **result)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/analysis/{analysis_id}", response_model=AnalysisResult)
def get_analysis(
    analysis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    record = db.get(Analysis, analysis_id)
    if record is None or record.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return record
