import os
import logging
import logging.handlers

from django.conf import settings


def password_filter(log: logging.LogRecord) -> int:
    if settings.LOG_PASS_FILTER in str(log.msg):
        return 0
    return 1


def create_file_log(file):
    if not os.path.isdir(settings.LOG_DIR):
        os.mkdir(settings.LOG_DIR)
    os.open(settings.LOG_FILE, flags=os.O_CREAT)
    return file


def init_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(settings.LOG_FORMAT))
    sh.setLevel(logging.DEBUG)
    sh.addFilter(password_filter)

    fh = logging.handlers.RotatingFileHandler(
        filename=create_file_log(file=settings.LOG_FILE)
    )
    fh.setFormatter(logging.Formatter(settings.LOG_FORMAT))
    fh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug(settings.LOG_MESSAGE)
