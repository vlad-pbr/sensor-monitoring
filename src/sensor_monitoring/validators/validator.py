from abc import ABC, abstractmethod

from pydantic import BaseModel

from sensor_monitoring.sensors import Sensor
from .types import SensorType


class Validator(BaseModel, ABC):
    type: SensorType
    valid_range: tuple[float, float]

    @property
    @abstractmethod
    def sensor(self) -> Sensor:
        pass

    @abstractmethod
    def validate_data(self) -> None:
        pass
