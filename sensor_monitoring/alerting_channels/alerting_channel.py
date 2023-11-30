from abc import ABC, abstractmethod
from logging import Handler


class AlertingChannel(ABC):

    @abstractmethod
    def get_logging_handler(self) -> Handler:
        pass
