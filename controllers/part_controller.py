from fastapi import APIRouter, Body, Depends, Path

from dto import PartToPodDto, PartDto
from services import PartService

part_router = APIRouter(prefix='/api/part', tags=['Part'])

@part_router.get('')
def get_available(
    part_service: PartService = Depends(PartService)
):
    return part_service.get_parts(available = True)

@part_router.patch('/{id}')
def patch_part(
    id: int = Path(),
    dto: PartToPodDto = Body(),
    part_service: PartService = Depends(PartService)
) -> PartDto:
    if dto.attach:
        return part_service.attach_to(id, dto.pod_id)
    else:
        return part_service.detach_from(id, dto.pod_id)