from pydantic import BaseModel, ConfigDict


class TopicDetailRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    sort_order: int


class SyllabusTopicRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    weightage: str | None
    sort_order: int
    details: list[TopicDetailRead]


class PaperRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    phase: str
    code: str
    title: str
    description: str
    duration_minutes: int | None
    max_marks: int | None
    sort_order: int
    topics: list[SyllabusTopicRead]


class SyllabusRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    year: int
    stream: str
    source_url: str
    papers: list[PaperRead]
