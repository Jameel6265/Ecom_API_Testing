from datetime import datetime
from config.config import LOG_FILE

def log_info(message):
    with open(LOG_FILE,'a') as log:
        log.write(f"[INFO] {datetime.now()} - {message}\n")

def log_error(message):
    with open(LOG_FILE,'a') as log:
        log.write(f"[INFO] {datetime.now()} - {message}\n")
