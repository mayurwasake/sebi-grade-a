from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.api.dependencies import get_db
from app.models import ExamCycle, Paper, SyllabusTopic
from app.schemas.syllabus import SyllabusRead

router = APIRouter(prefix="/syllabus", tags=["syllabus"])


@router.get("/{year}/{stream}", response_model=SyllabusRead, summary="Get a stream syllabus")
def get_syllabus(year: int, stream: str, db: Session = Depends(get_db)) -> ExamCycle:
    statement = (
        select(ExamCycle)
        .where(ExamCycle.year == year, ExamCycle.stream == stream)
        .options(
            selectinload(ExamCycle.papers)
            .selectinload(Paper.topics)
            .selectinload(SyllabusTopic.details)
        )
    )
    cycle = db.scalar(statement)
    if cycle is None:
        raise HTTPException(status_code=404, detail="Syllabus not found for this cycle and stream")
    cycle.papers.sort(key=lambda paper: (paper.phase, paper.sort_order))
    for paper in cycle.papers:
        paper.topics.sort(key=lambda topic: topic.sort_order)
    return cycle
