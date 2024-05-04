import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log',format = f"%(levelname)s : [ %(name)s ] : %(asctime)s : %(message)s " , filemode= "w",level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')