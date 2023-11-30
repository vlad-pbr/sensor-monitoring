from asyncio import Queue
from logging import getLogger
from typing import Never

from sensor_monitoring.models import Alert
from sensor_monitoring.types import AlertingChannelType


async def run_alert_service(alerts: Queue[Alert], alerting_channels: list[AlertingChannelType]) -> Never:
    """Reads alerts received from given queue and reports them to appropriate alerting channels."""

    logger = getLogger(__name__)
    logger.info("listening on sensor alerts...")

    # set up a separate logger exclusively for alerts and register external logging handlers with it
    alerting_logger = getLogger("Alert")
    alerting_logger.setLevel("WARNING")
    alerting_logger.propagate = False
    for alerting_channel in alerting_channels:
        alerting_logger.addHandler(alerting_channel.get_logging_handler())
        logger.debug(f"added '{alerting_channel.__class__.__name__}' alerting channel")

    while True:
        alert = await alerts.get()
        alerting_logger.warning(alert)
        logger.debug(f"received and distributed the following alert: {alert}")
