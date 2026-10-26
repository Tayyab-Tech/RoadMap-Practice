# Create a reusable logger function for multiple Python modules.
import logging

def get_logger(name):

    logger = logging.getLogger(name)

    if not logger.handlers:

        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler("Phase 1\\1.6 Reliability\\application.log")

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s : %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger