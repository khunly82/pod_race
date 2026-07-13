import random

from entities import Pod


class PodService:
    POD_NAMES = (
        "X-Wing",
        "TIE Fighter",
        "Millennium Falcon",
        "Slave I",
        "A-Wing",
        "Y-Wing",
        "Naboo Starfighter",
        "ARC-170",
        "Imperial Shuttle",
        "Ghost",
    )

    def generate_random_pod(self) -> Pod:
        return Pod(
            name=f"{random.choice(self.POD_NAMES)}-{random.randint(100, 999)}",
            base_speed=random.randint(30, 70),
            base_handling=random.randint(30, 55),
            shield=random.randint(10, 35),
        )
