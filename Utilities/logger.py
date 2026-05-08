import logging
import os
from datetime import datetime

def get_logger(test_name):

    log_dir = "Reports/Logs"
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    log_file = os.path.join(log_dir, f"{test_name}_{timestamp}.log")

    # ✅ Unique logger per test execution
    logger = logging.getLogger(f"{test_name}_{timestamp}")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # prevent duplicate logs

    # Common formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # ------------------ File Handler ------------------
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # ------------------ Console Handler ------------------
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger, log_file