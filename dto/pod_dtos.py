from __future__ import annotations

from dataclasses import dataclass

from .part_dtos import PartDto
from entities import Pod


@dataclass(frozen=True)
class PodDto:
    id: int
    name: str
    base_speed: int
    base_handling: int
    shield: int
    speed: int
    handling: int
    parts: list[PartDto]
    
    @classmethod
    def from_entity(cls: type[PodDto], entity: Pod):
        return cls(
            id=entity.id,
            name=entity.name,
            base_speed=entity.base_speed,
            base_handling=entity.base_handling,
            shield=entity.shield,
            speed=entity.base_speed + sum([p.boost_speed for p in entity.parts]),
            handling=entity.base_handling + sum([p.boost_handling for p in entity.parts]),
            parts=[PartDto.from_entity(p) for p in entity.parts]
        )