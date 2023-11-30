from typing import Type, Literal

from sensor_monitoring.sensors import Sensor, HumiditySensor
from .validator import Validator


class HumidityValidator(Validator):
    type: Literal["HumiditySensor"] = "HumiditySensor"

    def get_sensor_type(self) -> Type[Sensor]:
        return HumiditySensor
