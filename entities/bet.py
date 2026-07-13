from __future__ import annotations
from entities import Base
from enum import StrEnum, auto
from sqlalchemy import Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .race import Race
    from .pilot import Pilot

class Bet(Base):

    class Status(StrEnum):
        in_progress = auto()
        won = auto()
        lost = auto()

    __tablename__ = 'bets'
    id: Mapped[int] = mapped_column(primary_key=True)
    bettor_name: Mapped[str] = mapped_column()
    stake: Mapped[int] = mapped_column()
    odds: Mapped[int] = mapped_column()
    status: Mapped[Status] = mapped_column(SqlEnum(Status))

    race_id: Mapped[int] = mapped_column(ForeignKey('races.id'))
    pilot_id: Mapped[int] = mapped_column(ForeignKey('pilots.id'))

    race: Mapped[Race] = relationship(back_populates='bets')
    pilot: Mapped[Pilot] = relationship()