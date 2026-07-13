from __future__ import annotations

from sqlalchemy import ForeignKey
from entities import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pilot import Pilot
    from .part import Part

class Pod(Base):
    __tablename__ = 'pods'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    base_speed: Mapped[int] = mapped_column()
    base_handling: Mapped[int] = mapped_column()
    shield: Mapped[int] = mapped_column()

    pilot_id: Mapped[int] = mapped_column(ForeignKey('pilots.id'))
    pilot: Mapped[Pilot] = relationship(back_populates='pod')

    parts: Mapped[list[Part]] = relationship(back_populates='pod')