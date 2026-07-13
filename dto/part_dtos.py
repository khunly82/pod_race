from __future__ import annotations

from dataclasses import dataclass

from pydantic import BaseModel, Field

from entities import Part


@dataclass(frozen=True)
class PartDto:
    id: int
    name: str
    boost_speed: int
    boost_handling: int
    price: int

    @classmethod
    def from_entity(cls: type[PartDto], entity: Part):
        return cls(
            id=entity.id,
            name=entity.name,
            boost_speed=entity.boost_speed,
            boost_handling=entity.boost_handling,
            price=entity.price
        )
    
class PartToPodDto(BaseModel):
    pod_id: int = Field()
    attach: bool = Field(default=True)