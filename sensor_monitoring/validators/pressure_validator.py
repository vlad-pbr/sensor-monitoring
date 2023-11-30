from typing import Type, Literal

from sensor_monitoring.sensors import Sensor, PressureSensor
from .validator import Validator


class PressureValidator(Validator):
    type: Literal["PressureSensor"] = "PressureSensor"

    def get_sensor_type(self) -> Type[Sensor]:
        return PressureSensor
