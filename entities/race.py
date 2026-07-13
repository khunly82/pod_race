from __future__ import annotations
from entities import Base
from enum import StrEnum, auto
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .registration import registration

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pilot import Pilot
    from .bet import Bet

class Race(Base):

    class Dangerousness(StrEnum):
        easy = auto()
        medium = auto()
        mortal = auto()

    class RaceStatus(StrEnum):
        registration = auto()
        in_progress = auto()
        finished = auto()

    __tablename__ = 'races'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    dangerousness: Mapped[Dangerousness] = mapped_column(SqlEnum(Dangerousness))
    status: Mapped[RaceStatus] = mapped_column(SqlEnum(RaceStatus))
    registration_price: Mapped[int] = mapped_column()
    cash_prize: Mapped[int] = mapped_column()
    
    bets: Mapped[list[Bet]] = relationship(back_populates='race')
    pilots: Mapped[list[Pilot]] = relationship(secondary=registration)