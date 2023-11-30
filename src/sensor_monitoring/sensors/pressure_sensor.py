from asyncio import sleep
from typing import Self
from random import randint

from .sensor import Sensor


class PressureSensor(Sensor):
    """Outputs Pascal pressure values [500, 1500] after 3 seconds of delay."""

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> int:
        await sleep(3)
        return randint(500, 1500)
