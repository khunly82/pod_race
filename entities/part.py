from __future__ import annotations
from entities import Base
from enum import StrEnum, auto
from sqlalchemy import Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .pod import Pod

class Part(Base):
    class Type(StrEnum):
        engine = auto()
        thruster = auto()
        cockpit = auto()

    __tablename__ = 'parts'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    type: Mapped[Type] = mapped_column(SqlEnum(Type))
    boost_speed: Mapped[int] = mapped_column()
    boost_handling: Mapped[int] = mapped_column()
    price: Mapped[int] = mapped_column()

    pod_id: Mapped[Optional[int]] = mapped_column(ForeignKey('pods.id'), nullable=True)
    pod: Mapped[Optional[Pod]] = relationship(back_populates='parts')

