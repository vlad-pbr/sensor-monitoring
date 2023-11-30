from asyncio import TaskGroup, Queue, run as asyncio_run
from logging import getLogger, basicConfig
from pathlib import Path
from typing import Never, Annotated, Literal

from pydantic import BaseModel, Field

from .services import run_main_service, run_alert_service
from .types import ValidatorType


class Config(BaseModel):
    sensors: list[Annotated[ValidatorType, Field(discriminator="type")]]
    log_level: Literal["CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG", "NOTSET"]


async def _run(config_path: Path) -> Never:
    """
    Main entrypoint for this application. Must be executed in an event loop.
    """

    with config_path.open("rb") as config_file:
        config = Config.model_validate_json(config_file.read())

    # root logger configuration for the entire application
    basicConfig(level=config.log_level, format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
    logger = getLogger(__name__)
    logger.info(f"log level is set to '{config.log_level}'")

    logger.info("running sensor validation and alerting pipeline...")
    async with TaskGroup() as tg:
        alerts = Queue()
        tg.create_task(run_main_service(config.sensors, alerts))
        tg.create_task(run_alert_service(alerts))


def run(config_path: Path) -> Never:
    """Runs the alerting pipeline in an event loop."""

    asyncio_run(_run(config_path))
