from pathlib import Path

from logger import Logger


logger = Logger.instance(Path("log_config.yml"))

def main():
    logger.info("DONE")


if __name__ == "__main__":
    main()
