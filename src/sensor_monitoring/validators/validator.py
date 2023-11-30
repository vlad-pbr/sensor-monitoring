from abc import ABC, abstractmethod
from collections import namedtuple
from typing import Type

from pydantic import BaseModel

from sensor_monitoring.sensors import Sensor
from .types import SensorType


class Validator(BaseModel, ABC):
    type: SensorType
    valid_range: namedtuple('Range', ['min', 'max'])

    @abstractmethod
    def get_sensor_type(self) -> Type[Sensor]:
        pass

    @abstractmethod
    def is_valid_data(self, data: float) -> bool:
        pass
