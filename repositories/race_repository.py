from typing import Optional

from fastapi import Depends

from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session
from entities import get_session, Race


class RaceRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self._session = session

    def add(self, race: Race) -> Race:
        self._session.add(race)
        self._session.flush()
        return race
    
    def get_races(self) -> Sequence[Race]:
        stmt = select(Race).join(Race.pilots)
        return self._session.scalars(stmt).all()
    
    def get_race(self, race_id: int) -> Optional[Race]:
        stmt = select(Race).where(Race.id == race_id).join(Race.pilots, isouter=True).join(Race.bets, isouter=True)
        return self._session.scalars(stmt).first()
    
    def start_race(self, race: Race) -> Race:
        race.status = Race.RaceStatus.in_progress
        self._session.flush()
        return race

    def end_race(self, race: Race) -> Race:
        race.status = Race.RaceStatus.finished
        self._session.flush()
        return r
    