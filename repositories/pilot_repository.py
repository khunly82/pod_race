from typing import Optional

from fastapi import Depends
from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from entities import get_session, Pilot, Pod
from exceptions.value_errors import InvalidSortError

class PilotRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self._session = session

    def add(self, pilot: Pilot) -> Pilot:
        self._session.add(pilot)
        self._session.flush()
        return pilot

    def get_pilots(self, sort_order: Optional[str] = None) -> Sequence[Pilot]:
        stmt = select(Pilot).join(Pilot.pod).join(Pod.parts, isouter=True)
        if sort_order:
            if sort_order == 'credits':
                stmt = stmt.order_by(Pilot.credits)
            elif sort_order == '-credits':
                stmt = stmt.order_by(Pilot.credits.desc())
            else:
                raise InvalidSortError()
        return self._session.scalars(stmt).all()
    
    def update_credit(self, pilot: Pilot, amount: int) -> Pilot:
        pilot.credits += amount
        self._session.flush()
        return pilot