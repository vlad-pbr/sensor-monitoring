from sensor_monitoring.sensors import Sensor, TemperatureSensor
from .validator import Validator
from .types import SensorType


class TemperatureValidator(Validator):
    type: SensorType = "TemperatureSensor"

    @property
    def sensor(self) -> Sensor:
        return TemperatureSensor()

    def validate_data(self) -> None:
        pass
