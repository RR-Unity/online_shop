import logging
import sys

import graypy as graypy

from app.core.logging.handlers.loguruHandler import loguru_logger, loguru_format, LoguruHandler


class AppLogger(logging.Logger):
    def __init__(
        self,
        level: str = 'NOTSET',
        gl_host: str = None,
        gl_port: int = None,
        gl_facility: str = None,
    ):
        level = level.upper()
        super().__init__(__name__, level)

        if None not in [gl_host, gl_port, gl_facility]:
            g_handler = graypy.GELFUDPHandler(
                host=gl_host,
                port=gl_port,
                facility=gl_facility,
                extra_fields=True,
                level_names=level,
            )
            self.addHandler(g_handler)

        loguru_logger.remove()
        loguru_logger.add(sys.stdout, format=loguru_format, level=level)

        self.addHandler(LoguruHandler())
