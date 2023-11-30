from asyncio import sleep
from typing import Self
from random import randint

from .sensor import Sensor


class HumiditySensor(Sensor):
    """Outputs relative humidity (RH) percentage values [0, 100] after 0.5 seconds of delay."""

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> int:
        await sleep(0.5)
        return randint(0, 100)
