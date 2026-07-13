from typing import Optional

from fastapi import APIRouter, Body, Depends, Query

from dto import PilotAddDto, PilotDto
from services import PilotService
from fastapi_cache.decorator import cache

pilot_router = APIRouter(prefix='/api', tags=['Pilot'])

@pilot_router.post('/pilot', status_code=201)
def post(
        dto: PilotAddDto = Body(),
        pilot_service: PilotService = Depends(PilotService)
    ):
    # TODO INVALIDATE CACHE HERE
    pilot = pilot_service.add_pilot(dto)
    return pilot.id

@pilot_router.get('/pilot')
@cache(expire=60)
def get_pilots(
        sort_order: Optional[str] = Query(default=None),
        pilot_service: PilotService = Depends(PilotService)
    ) -> list[PilotDto]:
    print('---------------------LOAD DATA FROM POSTGRES-----------------------------')
    return pilot_service.get_pilots(sort_order)
    