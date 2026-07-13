from fastapi import Depends

from dto import PartDto
from exceptions.not_found_errors import NotFoundError
from exceptions.value_errors import AttachToPodError, DetachFromPodError
from repositories import PartRepository, PodRepository, PilotRepository


class PartService:
    def __init__(
        self, 
        part_repository: PartRepository = Depends(PartRepository),
        pod_repository: PodRepository = Depends(PodRepository),
        pilot_repository: PilotRepository = Depends(PilotRepository),
    ):
        self._part_repository = part_repository
        self._pod_repository = pod_repository
        self._pilot_repository = pilot_repository

    def get_parts(self, available: bool):
        return [PartDto.from_entity(p) for p in self._part_repository.get_parts(available)]
    
    def attach_to(self, part_id: int, pod_id: int) -> PartDto:
        part = self._part_repository.get_part(part_id)
        pod = self._pod_repository.get_pod(pod_id)

        if not part:
            raise NotFoundError()

        if part.pod_id != None:
            if part.pod_id == pod_id:
                raise AttachToPodError('This part is already attached to this pod')
            raise AttachToPodError(f'This part belongs to an other pod ({part.pod_id})')

        if not pod or len(pod.parts) >= 3:
            raise AttachToPodError('The pod is not available or does not have enough space')

        if pod.pilot.credits < part.price:
            raise AttachToPodError('The pilot does not have enough money to attach this part')
        
        self._pilot_repository.update_credit(pod.pilot, -part.price)
        part = self._part_repository.update_pod(part, pod)
        return PartDto.from_entity(part)
    
    def detach_from(self, part_id: int, pod_id: int) -> PartDto:
        part = self._part_repository.get_part(part_id)
        pod = self._pod_repository.get_pod(pod_id)

        if not part:
            raise NotFoundError()
        print(part_id)
        print('-------------------------', part.pod_id)
        print(part.__dict__)
        if part.pod_id != pod_id:
            raise DetachFromPodError(f'This part doen\'t belongs to this pod ({part.pod_id})')
        
        self._pilot_repository.update_credit(pod.pilot, part.price / 2)
        part = self._part_repository.update_pod(part, None)
        return PartDto.from_entity(part)