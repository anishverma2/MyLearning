import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)
#whenever we run this file it append the new logs to the txt file instead of overwriting
logger = logging.getLogger(__name__)

logger.info("This won't show up")
logger.warning("This will show up")
logger.debug('this is a debug message')
logger.critical('A critical error occured.')

'''
DEBUG - top level, shows all the things below this and the hierarchy goes same
INFO
WARNING
ERROR
CRITICAL
'''