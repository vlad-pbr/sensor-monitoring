import asyncio
from pathlib import Path
from typing import Never, Annotated, Union

from pydantic import BaseModel, Field

from sensor_monitoring.validators import TemperatureValidator


class Config(BaseModel):
    sensors: list[Annotated[Union[TemperatureValidator], Field(discriminator="type")]]


async def _run(config_path: Path) -> Never:
    with config_path.open("rb") as config_file:
        Config.model_validate_json(config_file.read())


def run(config_path: Path) -> Never:
    asyncio.run(_run(config_path))
