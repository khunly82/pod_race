from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, Field

from .pod_dtos import PodDto
from entities import Pilot


class PilotAddDto(BaseModel):
    name: str = Field()
    species: str = Field()

    def to_entity(self) -> Pilot:
        pilot = Pilot()
        pilot.name = self.name
        pilot.species = self.species
        return pilot

@dataclass(frozen=True)
class PilotDto:
    id: int
    name: str
    credits: int
    level: Pilot.Level
    status: Pilot.Status
    pod: PodDto

    @classmethod
    def from_entity(cls: type[PilotDto], entity: Pilot):
        return cls(
            id=entity.id,
            name=entity.name,
            credits=entity.credits,
            level=entity.level,
            status=entity.status,
            pod=PodDto.from_entity(entity.pod)
        )