from typing import Union

from .validators import TemperatureValidator
from .alerting_channels import EmailAlertingChannel

ValidatorType = Union[TemperatureValidator]
AlertingChannelType = Union[EmailAlertingChannel]
