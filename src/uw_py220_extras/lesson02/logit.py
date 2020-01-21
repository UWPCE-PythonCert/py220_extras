#!/usr/bin/env python

# change levels with (eg) set LOGURU_LEVEL="INFO"

from loguru import logger


def main():
    logger.info("Hello from loguru")
    logger.add("demo_{time}.log")
    logger.info("Put this in a file")
    logger.debug("Where am i?")
    logger.debug("But I am here")


if __name__ == "__main__":
    main()
