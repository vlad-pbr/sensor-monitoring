from typing import Type

from sensor_monitoring.sensors import Sensor, TemperatureSensor
from .types import SensorType
from .validator import Validator


class TemperatureValidator(Validator):
    type: SensorType = "TemperatureSensor"

    def get_sensor_type(self) -> Type[Sensor]:
        return TemperatureSensor

    def is_valid_data(self, data: float) -> bool:
        return self.valid_range.min <= data <= self.valid_range.max
