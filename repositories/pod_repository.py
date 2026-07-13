from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from entities import get_session, Pod


class PodRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self._session = session

    def get_pod(self, id: int) -> Optional[Pod]:
        stmt = select(Pod).filter(Pod.id == id).join(Pod.pilot).join(Pod.parts, isouter=True)
        print(stmt)
        return self._session.scalars(stmt).first()