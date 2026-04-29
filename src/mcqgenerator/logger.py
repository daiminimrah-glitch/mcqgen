
import os
from pathlib import Path
from datetime import datetime

# Base folder where logger.py is stored
BASE_DIR = Path(__file__).resolve().parent

# Logs folder inside project
LOG_DIR = BASE_DIR / "Logs"
LOG_DIR.mkdir(exist_ok=True)

# Unique timestamped log filename
LOG_FILE = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

# Full path to log file
LOG_PATH = LOG_DIR / LOG_FILE

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_PATH,
    format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s"
)