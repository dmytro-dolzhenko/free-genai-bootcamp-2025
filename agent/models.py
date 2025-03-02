from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class Example(BaseModel):
    japanese: str
    english: str

class VocabularyItem(BaseModel):
    word: str
    reading: str
    meaning: str
    type: str
    example: Example

class SongInfo(BaseModel):
    title: str
    artist: str
    lyrics_found: bool

class TutorResponse(BaseModel):
    status: str
    song_info: SongInfo
    vocabulary: List[VocabularyItem]