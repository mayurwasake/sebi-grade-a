import json
from datetime import datetime
from pathlib import Path

from sqlalchemy import select

from app.db.session import SessionLocal
from app.models import ExamCycle, Paper, SyllabusTopic, TopicDetail

CATALOG_PATH = Path(__file__).resolve().parents[2] / "catalog" / "sebi_2025_it.json"


def seed_syllabus() -> None:
    payload = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    with SessionLocal.begin() as session:
        cycle = session.scalar(
            select(ExamCycle).where(
                ExamCycle.year == payload["year"], ExamCycle.stream == payload["stream"]
            )
        )
        if cycle is None:
            cycle = ExamCycle(
                year=payload["year"],
                stream=payload["stream"],
                source_url=payload["source_url"],
                source_verified_at=datetime.fromisoformat(payload["source_verified_at"].replace("Z", "+00:00")),
            )
            session.add(cycle)
            session.flush()
        else:
            cycle.source_url = payload["source_url"]
            cycle.source_verified_at = datetime.fromisoformat(
                payload["source_verified_at"].replace("Z", "+00:00")
            )
            cycle.papers.clear()
            session.flush()

        for paper_index, paper_data in enumerate(payload["papers"]):
            paper = Paper(
                phase=paper_data["phase"],
                code=paper_data["code"],
                title=paper_data["title"],
                description=paper_data["description"],
                duration_minutes=paper_data.get("duration_minutes"),
                max_marks=paper_data.get("max_marks"),
                sort_order=paper_index,
            )
            cycle.papers.append(paper)
            for topic_index, topic_data in enumerate(paper_data["topics"]):
                topic = SyllabusTopic(
                    title=topic_data["title"],
                    weightage=topic_data.get("weightage"),
                    sort_order=topic_index,
                )
                paper.topics.append(topic)
                for detail_index, detail in enumerate(topic_data["details"]):
                    topic.details.append(TopicDetail(content=detail, sort_order=detail_index))
    print(f"Seeded {payload['year']} {payload['stream']} syllabus catalog")


if __name__ == "__main__":
    seed_syllabus()
