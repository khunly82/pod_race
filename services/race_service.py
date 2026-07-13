import asyncio

from fastapi import Depends

from dto import RaceAddDto, RaceDto
from entities import Race
from exceptions.not_found_errors import NotFoundError
from repositories import RaceRepository


class RaceService:
    def __init__(self, race_repository: RaceRepository = Depends(RaceRepository)):
        self._race_repository = race_repository

    def get_races(self) -> list[RaceDto]:
        return [r for r in self._race_repository.get_races()]
    
    def add_race(self, dto: RaceAddDto) -> RaceDto:
        race = dto.to_entity()
        race.status = Race.RaceStatus.registration
        self._race_repository.add(dto.to_entity())
        return RaceDto.from_entity(race)
    
    def start_race(self, race_id: int) -> Race:
        race = self._race_repository.get_race(race_id)
        if not race:
            raise NotFoundError()
        if race.status != Race.RaceStatus.registration or len(race.pilots) < 2:
            raise
        self._race_repository.start_race(race)
        return RaceDto.from_entity(race)
    
    async def simulate_race(self, race: Race):
        for i in range(20):
            await asyncio.sleep(1)
            print('step', i + 1)
        self._race_repository.end_race(race)
