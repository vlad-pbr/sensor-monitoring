from asyncio import sleep
from typing import Self

from .sensor import Sensor


class TemperatureSensor(Sensor):

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> float:
        await sleep(1)
        return 1000.0
