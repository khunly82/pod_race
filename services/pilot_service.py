from typing import Optional

from fastapi import Depends

from dto import PilotAddDto, PilotDto
from entities import Pilot
from repositories import PilotRepository
from .pod_service import PodService

class PilotService:
    def __init__(
            self, 
            pilot_repository: PilotRepository = Depends(PilotRepository),
            pod_service: PodService = Depends(PodService),
        ):
        self._pilot_repository = pilot_repository
        self._pod_service = pod_service

    def add_pilot(self, dto: PilotAddDto) -> PilotDto:
        pilot = dto.to_entity()
        pilot.credits = 1000
        pilot.level = Pilot.Level.beginer
        pilot.status = Pilot.Status.active
        pilot.pod = self._pod_service.generate_random_pod()
        return PilotDto.from_entity(self._pilot_repository.add(pilot))
    
    def get_pilots(self, search_order: Optional[str]) -> list[PilotDto]:
        return [PilotDto.from_entity(p) for p in self._pilot_repository.get_pilots(search_order)]
        