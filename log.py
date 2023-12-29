##### Logging #####
import logging
### Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('test.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add the handlers to the logger
handler.setFormatter(formatter)
logger.addHandler(handler)
