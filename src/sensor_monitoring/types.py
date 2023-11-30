from typing import Union

from .validators import TemperatureValidator, HumidityValidator
from .alerting_channels import EmailAlertingChannel

ValidatorType = Union[TemperatureValidator, HumidityValidator]
AlertingChannelType = Union[EmailAlertingChannel]
