from typing import Type

from sensor_monitoring.sensors import Sensor, TemperatureSensor
from .types import SensorType
from .validator import Validator


class TemperatureValidator(Validator):
    type: SensorType = "TemperatureSensor"

    def get_sensor_type(self) -> Type[Sensor]:
        return TemperatureSensor
