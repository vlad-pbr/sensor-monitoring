from logging import getLogger, Logger
from typing import Never
from asyncio import Queue, TaskGroup

from sensor_monitoring.types import ValidatorType


async def run_main_service(validators: list[ValidatorType], alerts: Queue[float]) -> Never:
    """
    Runs validation on sensors indicated by given validators. Puts invalid values into the given alerts queue.
    """

    async with TaskGroup() as tg:
        for validator in validators:
            tg.create_task(_run_sensor_validation(validator, alerts))


async def _run_sensor_validation(validator: ValidatorType, alerts: Queue[float]) -> Never:
    """Performs validation for a single sensor. Reports invalid values via alerting queue."""

    logger = getLogger(f"{validator.__class__.__name__}[{validator.get_sensor_type().__name__}]")
    logger.info(f"validating sensor values...")

    async for sensor_value in validator.get_sensor_type()():
        logger.debug(f"received value '{sensor_value}'")
        if not validator.is_valid_data(sensor_value):
            logger.debug(f"value '{sensor_value}' was deemed invalid")
            await alerts.put(sensor_value)