from asyncio import sleep
from typing import Self
from random import randint

from .sensor import Sensor


class TemperatureSensor(Sensor):
    """Outputs Fahrenheit temperature values [32, 212] after 1 second of delay."""

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> int:
        await sleep(1)
        return randint(32, 212)
