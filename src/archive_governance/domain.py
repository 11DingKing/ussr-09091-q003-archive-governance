from dataclasses import dataclass
from enum import StrEnum


class ImportState(StrEnum):
    PRECHECK = "precheck"
    CONFIRMED = "confirmed"
    ROLLED_BACK = "rolled_back"


@dataclass(frozen=True)
class ImportBatch:
    batch_id: str
    source_name: str
    state: ImportState = ImportState.PRECHECK
