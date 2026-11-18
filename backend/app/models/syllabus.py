from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ExamCycle(Base):
    __tablename__ = "exam_cycles"
    __table_args__ = (UniqueConstraint("year", "stream", name="cycle_year_stream"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    stream: Mapped[str] = mapped_column(String(80), index=True)
    source_url: Mapped[str] = mapped_column(String(500))
    source_verified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    papers: Mapped[list["Paper"]] = relationship(back_populates="cycle", cascade="all, delete-orphan")


class Paper(Base):
    __tablename__ = "syllabus_papers"
    __table_args__ = (UniqueConstraint("cycle_id", "phase", "code", name="paper_cycle_phase_code"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    cycle_id: Mapped[int] = mapped_column(ForeignKey("exam_cycles.id", ondelete="CASCADE"), index=True)
    phase: Mapped[str] = mapped_column(String(20), index=True)
    code: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(String(180))
    description: Mapped[str] = mapped_column(Text, default="")
    duration_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)
    max_marks: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)
    cycle: Mapped[ExamCycle] = relationship(back_populates="papers")
    topics: Mapped[list["SyllabusTopic"]] = relationship(back_populates="paper", cascade="all, delete-orphan")


class SyllabusTopic(Base):
    __tablename__ = "syllabus_topics"
    __table_args__ = (UniqueConstraint("paper_id", "title", name="topic_paper_title"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    paper_id: Mapped[int] = mapped_column(ForeignKey("syllabus_papers.id", ondelete="CASCADE"), index=True)
    title: Mapped[str] = mapped_column(String(220))
    weightage: Mapped[str | None] = mapped_column(String(30), nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)
    paper: Mapped[Paper] = relationship(back_populates="topics")
    details: Mapped[list["TopicDetail"]] = relationship(back_populates="topic", cascade="all, delete-orphan", order_by="TopicDetail.sort_order")


class TopicDetail(Base):
    __tablename__ = "syllabus_topic_details"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("syllabus_topics.id", ondelete="CASCADE"), index=True)
    content: Mapped[str] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)
    topic: Mapped[SyllabusTopic] = relationship(back_populates="details")
