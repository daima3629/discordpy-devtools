import logging
import sys

FORMATTER = logging.Formatter(
    fmt="[%(asctime)s | %(levelname)s] %(message)s",
    datefmt="%Y/%m/%d %a %H:%M:%S"
)


class StreamSwitchHandler(logging.Handler):
    def __init__(self, stderr_level: int = logging.ERROR, stdout_level: int = logging.DEBUG):
        super().__init__(stdout_level)
        self.stderr_level = stderr_level
        self.stdout_level = stdout_level
        self.setFormatter(FORMATTER)

    def emit(self, record):
        msg = self.format(record)
        if record.levelno >= self.stderr_level:
            print(msg, file=sys.stderr)
        elif record.levelno >= self.stdout_level:
            print(msg)
