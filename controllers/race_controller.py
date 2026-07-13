from fastapi import APIRouter, BackgroundTasks, Body, Depends, Path
from dto import RaceDto, RaceAddDto
from services import RaceService


race_router = APIRouter(prefix='/api/race', tags=['Race'])

@race_router.post('', status_code=201)
def add(
    dto: RaceAddDto = Body(),
    race_service: RaceService = Depends(RaceService)
) -> RaceDto:
    return race_service.add_race(dto)

@race_router.patch('/start/{id}')
def start(
    background_tasks: BackgroundTasks,
    id: int = Path(),
    race_service: RaceService = Depends(RaceService)
    
) -> RaceDto:
    race = race_service.start_race(id)
    background_tasks.add_task(race_service.simulate_race, race)
    return race
