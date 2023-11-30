from abc import ABC, abstractmethod
from typing import Type, NamedTuple, Self, Annotated

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator

from sensor_monitoring.sensors import Sensor
from .types import SensorType


class Range(NamedTuple):
    min: float
    max: float

    @classmethod
    def validate_valid_range(cls, _range: Self) -> Self:
        assert _range.min < _range.max, f"minimum value '{_range.min}' is lower than maximum value '{_range.max}'"
        return _range


class Validator(BaseModel, ABC):
    type: SensorType
    valid_range: Annotated[Range, AfterValidator(Range.validate_valid_range)]

    @abstractmethod
    def get_sensor_type(self) -> Type[Sensor]:
        pass
