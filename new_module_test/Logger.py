# #!/usr/bin/env python3
# # coding: utf-8

import sys
import logging
import os
import logging.handlers

LEVEL_DEBUG = 0
LEVEL_INFO = 1
LEVEL_WARN = 2
LEVEL_ERROR = 3

LOG_FILE =  os.path.dirname(__file__)  + '/log.log'

g_logger = None
stdout = None
stderr = None
# lock = Lock()
logging.basicConfig()


class StdRedir(object):
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, msg):
        if self.level == LEVEL_ERROR:
            self.logger.error(msg)
            stderr.write(msg)
        else:
            self.logger.info(msg)
            stdout.write(msg)

    def flush(self):
        pass


def initlog():
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    # stream_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    # stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)

    logger.setLevel(logging.WARN)

    global g_logger, stdout, stderr
    g_logger = logger
    stdout = sys.stdout
    stderr = sys.stderr

    out = StdRedir(logger, LEVEL_INFO)
    err = StdRedir(logger, LEVEL_WARN)

    sys.stdout = out
    sys.stderr = err


def info(msg, *args, **kwargs):
    g_logger.info(msg, *args, **kwargs)


def warn(msg, *args, **kwargs):
    g_logger.warn(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    g_logger.error(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    g_logger.debug(msg, *args, **kwargs)


initlog()

if __name__ == '__main__':
    for i in range(10):
        error("Testing %d, %s", 1, '我是中文')
    # debug("Testing %d, %s", 1, '我是中文')


# def info(msg, *args, **kwargs):
#     print(msg)
