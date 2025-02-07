import logging
from pathlib import Path
from datetime import datetime


class Logger:
    """A class to handle error logging with proper file handling and timestamps."""
    
    def __init__(self, log_dir: str = "./logs"):
        self.path_to_log_dir = Path(log_dir)
        self._setup_log_directory()
        self.logger_exiset:bool = False
        
        self.timestamp = datetime.now().strftime("%Y-%m-%d")
        self.log_file_path = self.path_to_log_dir / f"{self.timestamp}.log"
        
        if not self.log_exists(self.log_file_path):
            self._setup_logger()
            self.logger_exiset = True
        
    def log_exists(self, log_file_path: Path) -> bool:
        """Check if a log file exists."""
        return log_file_path.exists()
    
    def _setup_log_directory(self) -> None:
        """Create logs directory if it doesn't exist."""
        try:
            self.path_to_log_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise OSError(f"Failed to create log directory: {e}")
            
    def _setup_logger(self) -> None:
        """Configure the logger with proper formatting."""
        self.logger = logging.getLogger(f"ErrorLogger_{self.timestamp}")
        self.logger.setLevel(logging.ERROR)
        
        # Create file handler
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.ERROR)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(file_handler)
    
    def __enter__(self):
        """Context manager entry point."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point - ensures proper cleanup."""
        # Close all handlers
        for handler in self.logger.handlers:
            handler.close()
            self.logger.removeHandler(handler)
        
        if exc_type is not None:
            return False  # Re-raise any exceptions
        return True
    
    def log_error(self, error_message: str) -> None:
        """Log an error message with timestamp."""
        try:
            if self.logger_exiset:
                self.logger.error(error_message)
            else:
                with open(self.log_file_path, 'a') as f:
                    f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {error_message}\n")
                
        except Exception as e:
            print(f"Failed to log error: {e}")
    
    def log_maseg(self, message: str) -> None:
        """Log a message with timestamp."""
        try:
            if self.logger_exiset:
                self.logger.info(message)
            else:
                with open(self.log_file_path, 'a') as f:
                    f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        except Exception as e:
            print(f"Failed to log message: {e}")
            
    @property
    def log_file(self) -> Path:
        """Return the current log file path."""
        return self.log_file_path