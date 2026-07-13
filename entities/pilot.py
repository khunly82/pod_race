from __future__ import annotations
from entities import Base
from enum import StrEnum, auto
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pod import Pod

class Pilot(Base):

    class Status(StrEnum):
        active = auto()
        wounded = auto()
        dead = auto()

    class Level(StrEnum):
        beginer = auto()
        confirmed = auto()
        legend = auto()

    __tablename__ = 'pilots'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    species: Mapped[str] = mapped_column()
    credits: Mapped[int] = mapped_column()
    status: Mapped[Status] = mapped_column(SqlEnum(Status))
    level: Mapped[Level] = mapped_column(SqlEnum(Level))

    pod: Mapped[Pod] = relationship(back_populates='pilot')