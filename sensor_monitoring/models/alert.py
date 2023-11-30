from typing import NamedTuple


class Alert(NamedTuple):
    validator: str
    sensor: str
    value: int

    def __str__(self) -> str:
        return f"validator '{self.validator}' reported an abnormal value " \
               f"received from sensor '{self.sensor}': {self.value}"
