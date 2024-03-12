from datetime import datetime 
from appConfig import AppConfig
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.common.exceptions import TimeoutException
import os  
import locale
import shutil

class AppGenerales:    
    def __init__(self):
        self.appConfig = AppConfig()
    #__init__
    
    def fnAbrirPagina( self, wUrlPagina, wRutaDescarga = False):
        """Abriendo Pagina

        Args:
            wUrlPagina (text): _description_

        Returns:
            _type_: _description_
        """
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions") 
        options.add_argument("--disable-blink-features=AutomationControlled") 
        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('prefs', {
            "disable-notifications": True,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.default_content_setting_values.notifications": 2,
            'download.default_directory' : wRutaDescarga,
            "plugins.always_open_pdf_externally": True,
            "download.directory_upgrade":True,
            "download.prompt_for_download":False})
        options.add_experimental_option('detach', True)

        driver = webdriver.Chrome( self.appConfig.wChromeDriver, chrome_options=options)
        # driver = webdriver.Chrome( options=options)
             
        try:
            wait = WebDriverWait(driver, 180)
            driver.set_page_load_timeout(180)
            driver.get(wUrlPagina)
        except TimeoutException:
            driver.quit()
            driver = None
            pass 
        #fin driver
            
        return driver, wait
    #fnAbrirPagina
     
    def fnLimpiarCache( self, dv ):
        dv.execute_script("window.localStorage.clear();")
        dv.execute_script("window.sessionStorage.clear();")
    #fnLimpiarCache
    
    def fnCrearDirectorio(self, ruta_directorio ):
        os.makedirs( ruta_directorio )
    #fnCreandoDirectorio
    
    def fnConfigFecha(self, pTipo):
        """Configuración de fechas

        Args:
            pTipo (text): Condicion de fechas 
            
        Returns:
            text: Retorna valor segun la condición.
        """
        match pTipo:
            case 'AA' : return datetime.now().year                           #AÑO ACTUAL
            case 'FA' : return datetime.now().strftime('%Y-%m-%d')           #FECHA ACTUAL
            case 'HA' : return datetime.now().strftime('%H:%M:%S')           #HORA ACTUAL
            case 'FHA': return datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #FECHA HORA ACTUAL
        #math
    #fnConfigFecha
    
    def fnImprimir( self, pMensaje, pCantidad = 2 ):
        """Imprimir

        Args:
            pMensaje (text): Descripción del mensaje a imprimir en pantalla
            pCantidad (int, optional): cantidad de separador de espacio por defecto es 2.
        """
        print((' '*pCantidad) + '- '+pMensaje)
    #fnImprimir
     
    def fnSaltoLinea( self ):
        """Imprimir Salto de linea """
        print("\n" )
    #fnSaltoLineafnImprimir
 
    def fnImprimirTitulo(self, pTitulo ):
        """Imprimiendo titulo personalizado 
        Args:
            pTitulo (text): Descripción del titulo del proceso RPA
        """
        self.fnImprimir("-"*(len(pTitulo)+10))
        self.fnImprimir( (" "*5) + pTitulo.upper() )
        self.fnImprimir("-"*(len(pTitulo)+10))
    #fnImprimirTitulo
    
    def fnCopiarArchivo(self, pRutaArchivoActual, pRutaArchivoDestino):
        shutil.copy( pRutaArchivoActual, pRutaArchivoDestino )
    #fnCopiarArchivo
    
    def fnEliminarArchivo(self, pRutaArchivo):
        os.remove( pRutaArchivo )
    #fnEliminarArchivo
    
    def fnEliminarCarpeta( self, pRutaCarpeta ):
        shutil.rmtree( pRutaCarpeta  )
    #fnEliminarCarpeta
    
    def fnCrearDirectorio(self, pRutaDirectorio ):
        os.makedirs( pRutaDirectorio )
    #fnCreandoDirectorio
    
    def fnMoverArchivo(self, pRutaArchivoActual, pRutaArchivoDestino):
        shutil.move( pRutaArchivoActual, pRutaArchivoDestino )
    #fnMoverArchivo
    
    def fnExisteArchivo(self, pRutaArchivo ):
        return True if os.path.isfile( pRutaArchivo ) else False
    #fnExisteArchivo
    
    ######## Convertidores de Fecha
    def fnConvertirFecha( self, pFecha, pSeparadorAnt = '/', pSeparadorAct = '-' ):
        """Retornar la fecha convertida"""

        return pSeparadorAct.join(pFecha.split(pSeparadorAnt)[::-1])
    #fnFecConvertir
    
    def fnConvertirFechaHora( self, pFechaHora, pSeparadorAnt = '/', pSeparadorAct = '-' ):
        """Retornar la fecha hora convertida"""

        if pFechaHora:
            wFecha,wHora = pFechaHora.split(' ')
            return self.fnConvertirFecha( wFecha, pSeparadorAnt, pSeparadorAct ) + ' ' + wHora
        return ''
    #fnFecConvertir
    
    
    def fnRetormarMesTextoPorNro( self, wMes) :
        arrMeses = {
            'enero' : '01'
            ,'febrero' : '02'
            ,'marzo' : '03'
            ,'abril' : '04'
            ,'mayo' : '05'
            ,'junio' : '06'
            ,'julio' : '07'
            ,'agosto' : '08'
            ,'setiembre' : '09'
            ,'septiembre' : '09'
            ,'octubre' : '10'
            ,'noviembre' : '11'
            ,'diciembre' : '12'
            
            ,'ene' : '01'
            ,'feb' : '02'
            ,'mar' : '03'
            ,'marz' : '03'
            ,'abr' : '04'
            ,'may' : '05'
            ,'jun' : '06'
            ,'jul' : '07'
            ,'ago' : '08'
            ,'set' : '09'
            ,'oct' : '10'
            ,'nov' : '11'
            ,'dic' : '12'
        }
        return arrMeses[str(wMes).lower()]
    #fnRetormarMesTextoPorNro
    
    def fnConvertirFechaTextoMes( self, pFecha, inicial_mayuscula = True  ):
        """Retornar la fecha convertida
            Ejm: '13/01/2023' => '13 enero 2023'
        """
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        datetime.strptime(pFecha, '%d/%m/%Y')
        fecha_obj = datetime.strptime(pFecha, '%d/%m/%Y')
        nombre_mes = fecha_obj.strftime('%B') 
        
        return fecha_obj.strftime(f'%d {nombre_mes.capitalize() if inicial_mayuscula else nombre_mes } %Y')
    #fnFecConvertir
    
    def fnRetornarDiffFechas( self, wFecha ):
        wFechaIniTermino = self.app_general.fnConvertirFecha(wFecha, '-', '/') 
        
        wArrFechaBusqueda = [
            wFechaIniTermino                                                                                                               # 01/11/2023
            ,str(self.fnConvertirFechaTextoMes(wFechaIniTermino)).lower()                                                                  # 01 noviembre 2023
            ,str(self.fnConvertirFechaTextoMes(wFechaIniTermino)).lower().replace(' '+wFechaIniTermino.split('/')[-1],'')                  # 01 noviembre
            ,str(self.fnConvertirFechaTextoMes(wFechaIniTermino)).lower().replace(' '+wFechaIniTermino.split('/')[-1],'').replace(' ','-') # 01-noviembre
        ]
        
        return wArrFechaBusqueda
        
    #fnRetornarDiffFechas
    
    def fnRetornarFechaLimpia( self, wFecha ):
        
        if str(wFecha).lower() in ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'):
            return ''
        #fin if 
        
        if len(wFecha) < 9:
            return ''
        #fin if 
        
        wFechaTmp = str(wFecha).replace('-', '/').strip().lower()
        wFechaTmp = wFechaTmp.replace(' de ', ' ').strip()
        # wFechaTmp = wFechaTmp.replace(' de ', '/').strip()
        wFechaTmp = wFechaTmp.replace(' / ', '/').strip()
        wFechaTmp = wFechaTmp.replace(' - ', '/').strip()
        wFechaTmp = wFechaTmp.replace('providencia:', '').strip()
        wFechaTmp = wFechaTmp.replace('/salvo 1', '').strip()
        wFechaTmp = wFechaTmp.replace('/salvo 2', '').strip()
        wFechaTmp = wFechaTmp.replace('/salvo 3', '').strip()  
        wFechaTmp = wFechaTmp.replace('.', '/').strip()
        wFechaTmp = wFechaTmp.replace('  ', ' ').strip()
        
        
        #convertir de 01 enero 2023 a 01/01/2023
        if '/' in wFechaTmp:
            if  "estado no/" in wFechaTmp: 
                wArrFechaTmp = (wFechaTmp[15:] if "estado no/ " in wFechaTmp else wFechaTmp[14:]).split(' ')
                wFechaTmp = wArrFechaTmp[1].zfill(2) + '/' + self.fnRetormarMesTextoPorNro( wArrFechaTmp[0] ) + '/' +  wArrFechaTmp[2]
            elif "publicado" in wFechaTmp:
                wArrFechaTmp = wFechaTmp.split('publicado')[1].strip().split(' ')
                wArrFechaTmp = wArrFechaTmp[0] + ' ' + wArrFechaTmp[1]
            elif len(wFechaTmp.split('/')[1]) > 2:
                wFechaTmp = wFechaTmp.split('/')[0].strip().zfill(2) +'/'+ self.fnRetormarMesTextoPorNro(wFechaTmp.split('/')[1].strip()) +'/'+ wFechaTmp.split('/')[2].strip()
            elif len(wFechaTmp.split('/')) == 3:
                if len(wFechaTmp.split('/')[-1]) == 2 and len(wFechaTmp.split('/')[0]) == 2: 
                    wFechaTmp = wFechaTmp.split('/')[0].zfill(2) + '/' + wFechaTmp.split('/')[1].zfill(2) + '/'  + ( str(self.fnConfigFecha('AA'))[:2] + wFechaTmp.split('/')[2] if len(wFechaTmp.split('/')[2] ) == 2 else wFechaTmp.split('/')[2]  )
                elif len(wFechaTmp.split('/')[-1]) == 4 and len(wFechaTmp.split('/')[0]) == 1: 
                    wFechaTmp = wFechaTmp.split('/')[0].zfill(2) + '/' +  wFechaTmp.split('/')[1].zfill(2) + '/'  + wFechaTmp.split('/')[2]
                #fin if 
            #fin if            
        # elif "estado no/" in wFechaTmp: 
        #     wArrFechaTmp = (wFechaTmp[15:] if "estado no/ " in wFechaTmp else wFechaTmp[14:]).split(' ')
        #     wFechaTmp = wArrFechaTmp[1].zfill(2) + '/' + self.fnRetormarMesTextoPorNro( wArrFechaTmp[0] ) + '/' +  wArrFechaTmp[2]
        #fin if  
        
        return wFechaTmp 
    #fnRetornarFechaLimpia
     