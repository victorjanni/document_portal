import os
import logging
import structlog
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        # Ensure logs directory exits
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # Timestamped log file, for persistence
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)
    
    def get_logger(self, name=__file__):
        logger_name = os.path.basename(name)