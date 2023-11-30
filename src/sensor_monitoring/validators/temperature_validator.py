from typing import Type, Literal

from sensor_monitoring.sensors import Sensor, TemperatureSensor
from .validator import Validator


class TemperatureValidator(Validator):
    type: Literal["TemperatureSensor"] = "TemperatureSensor"

    def get_sensor_type(self) -> Type[Sensor]:
        return TemperatureSensor
