import logging, os
from appGenerales import AppGenerales

class Logger:
    def __init__(self, log_titulo):
        self.appGeneral = AppGenerales()
        
        self.log_titulo = log_titulo
        self.logger = self._create_logger()

    def _create_logger(self ):
       
        logger = logging.getLogger( self.log_titulo )
        logger.setLevel(logging.DEBUG)
        
        if not os.path.exists( self.appGeneral.appConfig.wRutaLog.replace( self.appGeneral.appConfig.wRutaLog.split('\\')[-1] , '') ):
            self.appGeneral.fnCrearDirectorio( self.appGeneral.appConfig.wRutaLog.replace( self.appGeneral.appConfig.wRutaLog.split('\\')[-1] , '')   )
        #fin if
        
        file_handler = logging.FileHandler( self.appGeneral.appConfig.wRutaLog.replace('.log', ('-'+self.appGeneral.fnConfigFecha('FA').replace('-','')+'.log')) )
        file_handler.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
         
        return logger

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)
#Logger

