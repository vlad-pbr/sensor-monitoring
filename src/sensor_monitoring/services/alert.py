from asyncio import Queue
from logging import getLogger
from typing import Never


async def run_alert_service(alerts: Queue[float]) -> Never:
    logger = getLogger(__name__)
    logger.info("listening on sensor alerts...")

    while True:
        logger.warning(await alerts.get())
