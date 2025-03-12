from enum import Enum, auto
from bedrocked.reporting.logged import logger

class ReportTypes(Enum):
    logger.error("NotYetImplementedYet: 'Reporter' features are unavailable.")

def report(report_type: str, *args, **kwargs):
    raise NotImplementedError("The central reporter has not yet been implemented.")
