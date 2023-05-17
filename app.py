import logging
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.basicConfig(level=logging.DEBUG)  # Set the desired logging level (e.g., DEBUG, INFO, WARNING, ERROR)
    logger = logging.getLogger(__name__)
    logger.info("Your log message")  # for standard output
if __name__ == '__main__':
    app.run()




