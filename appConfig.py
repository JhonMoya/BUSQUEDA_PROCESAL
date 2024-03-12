import configparser, uuid, socket

class AppConfig( ):
    def __init__( self ):
        self.dataConfig = configparser.ConfigParser() 
        self.fnAjustesInformacion( )
    #__init__

    def fnAjustesInformacion( self ):   
        self.dataConfig.read('C:\ROBOT\CONFIG\config-juzgadoMunicipalEjec01.ini') 
        
        # [config]
        self.wChromeDriver     = self.dataConfig.get("config", "chromedriver").strip()
        self.wCarpetaPrincipal = self.dataConfig.get("config", "carpeta_principal").strip()
        self.wTiempoEjecucion  = self.dataConfig.get("config", "tiempo_ejecucion").strip()  
        self.wCodAgente        = self.dataConfig.get("config", "cod_agente").strip() # proceso cuando se implemente +1 agente 
        self.wNroAgente        = self.dataConfig.get("config", "nro_agentes").strip() # proceso cuando se implemente +1 agente
        
        # [api]
        self.wRutaApi        = self.dataConfig.get("api", "ruta")
        
        # [juzgado-municipal]
        self.wPagConsumir       = self.dataConfig.get("juzgado-municipal", 'pagina_consumir').strip() 
        self.wRutaLog           = self.dataConfig.get("juzgado-municipal", "ruta_log").strip() 
        self.wRutaDescPdf       = self.wCarpetaPrincipal + self.dataConfig.get("juzgado-municipal", "ruta_desc_pdf").strip()
        self.wRutaDescPdfFin    = self.wCarpetaPrincipal + self.dataConfig.get("juzgado-municipal", "ruta_desc_pdfFin").strip()
        self.wRutaDescPdfFinV2  = self.wCarpetaPrincipal + self.dataConfig.get("juzgado-municipal", "ruta_desc_pdfFinV2").strip()
        self.wRutaDescPdfFinZip = self.wCarpetaPrincipal + self.dataConfig.get("juzgado-municipal", "ruta_desc_pdfFinZip").strip()
        self.wRutaDescPdfSel    = self.wCarpetaPrincipal + self.dataConfig.get("juzgado-municipal", "ruta_desc_pdfSel").strip()
        
        # [juzgado-municipal-drive]
        self.wRutaAlmPdfDrive   = self.dataConfig.get("juzgado-municipal-drive", "ruta_almpend_drive").strip()
    #fnAjustesInformacion