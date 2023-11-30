from asyncio import Queue, TaskGroup
from logging import getLogger
from typing import Never, cast

from sensor_monitoring.models import Alert
from sensor_monitoring.types import ValidatorType


async def run_main_service(validators: list[ValidatorType], alerts: Queue[Alert]) -> Never:
    """
    Runs validation on sensors indicated by given validators. Puts invalid values into the given alerts queue.
    """

    async with TaskGroup() as tg:
        for validator in validators:
            tg.create_task(_run_sensor_validation(validator, alerts))


async def _run_sensor_validation(validator: ValidatorType, alerts: Queue[Alert]) -> Never:
    """Performs validation for a single sensor. Reports invalid values via alerting queue."""

    logger = getLogger(f"{validator.__class__.__name__}[{validator.get_sensor_type().__name__}]")
    logger.info(f"validating sensor values...")

    async for sensor_value in validator.get_sensor_type()():
        # PyCharm claims that `sensor_value` is a coroutine instead of the value itself due to an open bug
        # see 'https://youtrack.jetbrains.com/issue/PY-60714/PyCharm-does-not-understand-async-iterators'
        sensor_value = cast(int, sensor_value)

        logger.debug(f"received value '{sensor_value}'")
        if not validator.valid_range.min <= sensor_value <= validator.valid_range.max:
            logger.debug(f"value '{sensor_value}' was deemed invalid")
            await alerts.put(
                Alert(
                    validator=validator.__class__.__name__,
                    sensor=validator.get_sensor_type().__name__,
                    value=sensor_value
                )
            )
