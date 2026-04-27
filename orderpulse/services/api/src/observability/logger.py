import logging
from typing import Any


def get_logger(name: str = "orderpulse") -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    return logger


def log_json(logger: logging.Logger, **fields: Any) -> None:
    logger.info(str(fields))
