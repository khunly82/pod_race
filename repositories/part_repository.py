from typing import Optional

from fastapi import Depends
from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from entities import get_session
from entities import Part, Pod


class PartRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self._session = session


    def add_part(self, part: Part) -> Part:
        self._session.add(part)
        self._session.flush()
        return part
    
    def get_part(self, id: int) -> Optional[Part]:
        stmt = select(Part).filter(Part.id == id)
        return self._session.scalars(stmt).first()

    def get_parts(self, available: bool) -> Sequence[Part]:
        stmt = select(Part)
        if available:
            stmt = stmt.filter(Part.pod_id == None)
        return self._session.scalars(stmt).all()
    
    def update_pod(self, part: Part, pod: Pod):
        part.pod = pod
        self._session.flush()
        return part