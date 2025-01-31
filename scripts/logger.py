import logging

# Configure logging
logging.basicConfig(filename="../logs/nifi_process.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_message(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    elif level == "warning":
        logging.warning(message)

if __name__ == "__main__":
    log_message("NiFi process started", "info")
