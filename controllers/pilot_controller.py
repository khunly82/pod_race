from typing import Optional

from fastapi import APIRouter, Body, Depends, Query
from fastapi_cache import FastAPICache

from dto import PilotAddDto, PilotDto
from services import PilotService
from fastapi_cache.decorator import cache

pilot_router = APIRouter(prefix='/api', tags=['Pilot'])

@pilot_router.post('/pilot', status_code=201)
async def post(
        dto: PilotAddDto = Body(),
        pilot_service: PilotService = Depends(PilotService)
    ):
    pilot = pilot_service.add_pilot(dto)
    # EXERCICE: 
    # TODO INVALIDATE CACHE HERE
    await FastAPICache.clear(namespace='pilot')
    return pilot.id

@pilot_router.get('/pilot')
@cache(expire=300, namespace='pilot')
def get_pilots(
        sort_order: Optional[str] = Query(default=None),
        pilot_service: PilotService = Depends(PilotService)
    ) -> list[PilotDto]:
    print('---------------------LOAD DATA FROM POSTGRES-----------------------------')
    return pilot_service.get_pilots(sort_order)
    