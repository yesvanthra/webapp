
import logging
from flask import Flask

app = Flask(__name__)

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler and set the logging level
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a log formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


@app.route('/')
def hello_world():
    logger.info('Hello, World!')  # Log the message instead of printing
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()




