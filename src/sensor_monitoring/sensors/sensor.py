from abc import ABC, abstractmethod
from typing import Self


class Sensor(ABC):

    @abstractmethod
    def __aiter__(self) -> Self:
        pass

    @abstractmethod
    async def __anext__(self) -> float:
        pass
