from logging import Handler
from logging.handlers import SMTPHandler
from typing import Annotated, Literal

from pydantic import BaseModel, Field

from .alerting_channel import AlertingChannel


class EmailAlertingChannel(BaseModel, AlertingChannel):
    type: Literal["email"] = "email"

    host: Annotated[str, Field(min_length=1)]
    port: Annotated[int, Field(ge=1024, le=65535)]

    def get_logging_handler(self) -> Handler:
        return SMTPHandler(
            mailhost=(self.host, self.port),
            fromaddr="sensoralerts@example.com",
            toaddrs="user@example.com",
            subject="Sensor Alert"
        )
