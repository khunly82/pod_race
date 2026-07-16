from __future__ import annotations
from dataclasses import dataclass

from pydantic import BaseModel, Field

from dto import PilotDto
from entities import Race


@dataclass
class RaceDto:
    id: int
    name: str
    status: Race.RaceStatus
    dangerousness: Race.Dangerousness
    pilots: list[PilotDto]

    @classmethod
    def from_entity(cls: type[RaceDto], entity: Race):
        return cls(
            id=entity.id,
            name=entity.name,
            status=entity.status,
            dangerousness=entity.dangerousness,
            pilots=[PilotDto.from_entity(p) for p in entity.pilots]
        )

class RaceAddDto(BaseModel):
    name: str = Field(max_length=50)
    dangerousness: Race.Dangerousness = Field()

    def to_entity(self) -> Race:
        race = Race()
        race.name = self.name
        race.dangerousness = self.dangerousness
        return race