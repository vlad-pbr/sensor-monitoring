from abc import ABC, abstractmethod
from typing import Type, Annotated

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator

from sensor_monitoring.models import Range
from sensor_monitoring.sensors import Sensor


class Validator(BaseModel, ABC):
    valid_range: Annotated[Range, AfterValidator(Range.validate_valid_range)]

    @abstractmethod
    def get_sensor_type(self) -> Type[Sensor]:
        pass
