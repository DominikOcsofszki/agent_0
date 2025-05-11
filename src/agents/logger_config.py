import logging


def setup_logger(
    name: str, log_file: str = "fastmcp.log", level=logging.INFO
) -> logging.Logger:
    # formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    # formatter = logging.Formatter(f"[{name} %(asctime)s] %(message)s")
    formatter = logging.Formatter(f"[{name}] %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        # logger.info("========LOGGER-SETUP============")

    return logger
