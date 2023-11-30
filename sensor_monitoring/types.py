from typing import Union

from .validators import TemperatureValidator, HumidityValidator, PressureValidator
from .alerting_channels import EmailAlertingChannel

ValidatorType = Union[TemperatureValidator, HumidityValidator, PressureValidator]
AlertingChannelType = Union[EmailAlertingChannel]
