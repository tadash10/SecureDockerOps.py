import logging

def setup_logging():
    # Configure the logging format, level, and handlers
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),
            # Add additional handlers as needed (e.g., log to a file)
        ]
    )

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

# Add other logging functions as needed
