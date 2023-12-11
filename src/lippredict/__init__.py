import os
import sys
import logging
import time

current_time = time.time()
human_readable_time = time.strftime("%b_%Y__%I_%M_%p", time.localtime())

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, f"{  human_readable_time}.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("LipPredictLogger")
