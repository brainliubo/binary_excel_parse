import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('output.log',mode = "w")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(module)s- %(lineno)d-%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
