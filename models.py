from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Module:
    code: str
    name: str
    type: str  # 'PROG', 'MATH', 'THEORY', 'MIXED', 'LAB', 'PROJECT', 'PRACTICAL'
    credits: int
    part: str  # 'I', 'II', 'III', 'IV'
    semester: Optional[int]  # 1, 2, or None (e.g., for attachment)
    is_elective: bool = False

@dataclass
class TranscriptEntry:
    module: Module
    mark: float

@dataclass
class Programme:
    name: str
    code: str
    modules: List[Module]

@dataclass
class StudentProfile:
    programme: Programme
    current_part: str
    transcript_end_part: str
    transcript_end_semester: Optional[int]
    transcript: List[TranscriptEntry] = field(default_factory=list)
    
    def get_module_mark(self, module_code: str) -> Optional[float]:
        for entry in self.transcript:
            if entry.module.code == module_code:
                return entry.mark
        return None
