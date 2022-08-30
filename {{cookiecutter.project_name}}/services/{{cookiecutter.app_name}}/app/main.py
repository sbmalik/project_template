import logging

logging.basicConfig(
    level=logging.INFO, format="%(levelname)s: PID %(process)d: %(message)s"
)
logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")

logging.info(f"Welcome to {{cookiecutter.app_name}}")