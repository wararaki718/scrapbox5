from pathlib import Path

from logger import CustomLogger


logger = CustomLogger.instance(__name__, Path("log_config.yml"))


def main():
    logger.info("DONE")


if __name__ == "__main__":
    main()
