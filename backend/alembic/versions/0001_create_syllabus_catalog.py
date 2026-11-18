"""Create the versioned syllabus catalog.

Revision ID: 0001_syllabus
Revises:
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_syllabus"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "exam_cycles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("stream", sa.String(80), nullable=False),
        sa.Column("source_url", sa.String(500), nullable=False),
        sa.Column("source_verified_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("year", "stream", name="uq_exam_cycles_cycle_year_stream"),
    )
    op.create_index("ix_exam_cycles_year", "exam_cycles", ["year"])
    op.create_index("ix_exam_cycles_stream", "exam_cycles", ["stream"])
    op.create_table(
        "syllabus_papers",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cycle_id", sa.Integer(), sa.ForeignKey("exam_cycles.id", ondelete="CASCADE"), nullable=False),
        sa.Column("phase", sa.String(20), nullable=False), sa.Column("code", sa.String(30), nullable=False),
        sa.Column("title", sa.String(180), nullable=False), sa.Column("description", sa.Text(), nullable=False),
        sa.Column("duration_minutes", sa.Integer(), nullable=True), sa.Column("max_marks", sa.Integer(), nullable=True),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.UniqueConstraint("cycle_id", "phase", "code", name="uq_syllabus_papers_paper_cycle_phase_code"),
    )
    op.create_index("ix_syllabus_papers_cycle_id", "syllabus_papers", ["cycle_id"])
    op.create_index("ix_syllabus_papers_phase", "syllabus_papers", ["phase"])
    op.create_table(
        "syllabus_topics", sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("paper_id", sa.Integer(), sa.ForeignKey("syllabus_papers.id", ondelete="CASCADE"), nullable=False),
        sa.Column("title", sa.String(220), nullable=False), sa.Column("weightage", sa.String(30), nullable=True),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.UniqueConstraint("paper_id", "title", name="uq_syllabus_topics_topic_paper_title"),
    )
    op.create_index("ix_syllabus_topics_paper_id", "syllabus_topics", ["paper_id"])
    op.create_table(
        "syllabus_topic_details", sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("topic_id", sa.Integer(), sa.ForeignKey("syllabus_topics.id", ondelete="CASCADE"), nullable=False),
        sa.Column("content", sa.Text(), nullable=False), sa.Column("sort_order", sa.Integer(), nullable=False),
    )
    op.create_index("ix_syllabus_topic_details_topic_id", "syllabus_topic_details", ["topic_id"])


def downgrade() -> None:
    op.drop_table("syllabus_topic_details")
    op.drop_table("syllabus_topics")
    op.drop_table("syllabus_papers")
    op.drop_table("exam_cycles")
