#!/usr/bin/env python
# encoding: utf-8
from appJuzgado import JuzgadoBase
from appApiModel import ApiModel
 

import time, os, sys
from selenium.webdriver.common.by import By  
import pandas as pd
import json, re
import zipfile
from selenium.webdriver.common.keys import Keys 
from pathlib import Path

def fnActualizarHtmlModelo09v1( driver, juzgado, datos ):
    for indice, eti_li in enumerate( driver.find_elements(By.XPATH, app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado).xpath_pest) ): 
        if str(datos['Mes']).lower().strip() in str(eti_li.text).lower().strip():
            eti_li.click()
            time.sleep(0.5)
            
            elemento_tabla = app_juzgado.fnRetornarElementoTabla( app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado).xpath_tab.replace('MES',str(indice+1)), driver )[0]
            
            cont_tabla = 1
            for tr in elemento_tabla.find_elements(By.TAG_NAME, 'tr')[1:]: 
                if  len(tr.find_elements(By.XPATH,'td')) >= int(re.findall(r'\[(\d+)\]', 'td[2]')[0]):
                    elem_fecha_estado = tr.find_element(By.XPATH,'td[2]')
                    fecha_estado = elem_fecha_estado.text
                    etiqueta_a   = elem_fecha_estado.get_attribute('innerHTML') 
                    
                    table_reemplazar = app_juzgado.fnRetornarElementoTabla( app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado).xpath_tab.replace('MES',str(indice+1)), driver )[cont_tabla]
                    for tr_reemplazar in table_reemplazar.find_elements(By.TAG_NAME, 'tr')[2:]: 
                        if  len(tr_reemplazar.find_elements(By.XPATH,'td')) >= int(re.findall(r'\[(\d+)\]', 'td[2]')[0]):
                            elemento_radicado = tr_reemplazar.find_element(By.XPATH,'td[1]')
                            if len(elemento_radicado.find_elements(By.TAG_NAME,'a')) == 0:
                                nro_radicado = elemento_radicado.text
                                etiqueta_radicado = etiqueta_a.replace(fecha_estado,nro_radicado)
                                
                                driver.execute_script("arguments[0].innerHTML = arguments[1];", elemento_radicado, etiqueta_radicado)
                            #fin if 
                        #fin if 
                    #fin for  
                #fin if 
                
                cont_tabla+=1
            #fin for  
            
            break
        #fin if  
    #fin for   
#fnActualizarHtmlModelo09v1

def fnActualizarHtmlModelo09v2( driver, juzgado, datos, columna_donde_ira_enlace_estado = 'td[1]' ):
    for indice, eti_li in enumerate( driver.find_elements(By.XPATH, app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado).xpath_pest) ):
        try:
            if str(datos['Mes']).lower() in str(eti_li.text).strip().lower():
                eti_li.click()
                time.sleep(0.5)
                
                for eti_p in driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/p'):
                    try: 
                        if len( eti_p.find_elements(By.TAG_NAME,'a')) > 0:
                            eti_a = eti_p.find_element(By.TAG_NAME,'a')
                            
                            cadena = eti_a.get_attribute("href")
                            posicion_codigo = cadena.find("/", cadena.find("/", cadena.find("/", cadena.find("/", cadena.find("/", cadena.find("/") + 1) + 1) + 1) + 1) + 1) + 1
                            ubicacion_codigo = cadena[:posicion_codigo]
                            
                            desc_eti_a = eti_a.text
                            etiqueta_a = eti_a.get_attribute('outerHTML')
                            
                            for table in app_juzgado.fnRetornarElementoTabla( app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado).xpath_tab.replace('MES',str(indice+1)), driver ):
                                for tr in table.find_elements(By.TAG_NAME, 'tr')[1:]: 
                                    
                                    ele_archivo = tr.find_element(By.XPATH,'td[7]')
                                    if len(ele_archivo.find_elements(By.TAG_NAME,'a'))>0:
                                        ele_eti_a = ele_archivo.find_element(By.TAG_NAME,'a')
                                        if ubicacion_codigo in (ele_eti_a).get_attribute('href'):
                                            elem_rad = tr.find_element(By.XPATH, columna_donde_ira_enlace_estado )
                                            radicado = etiqueta_a.replace( desc_eti_a, elem_rad.text).strip()
                                            
                                            driver.execute_script("arguments[0].innerHTML = arguments[1];", elem_rad, radicado)
                                        #fin if 
                                    #fin if 
                                
                                #fin for
                            #fin for 
                        #fin if
                    except:
                        pass
                #fin for 
            #fin if 
        except:
            pass
    #fin for
#fnActualizarHtmlModelo09v2

def fnProcesarDatos( driver, objDatos, app_apiModel, app_juzgado, app_general, app_config, app_log ):
    try:
        # Variables
        wArrDatosGenerales = app_juzgado.fnRetornarDatosAgrupados( objDatos, 'EE' )
        wTotCedulas        = len(objDatos) 
        wMes               = ''
        wCont              = 1
    
        app_general.fnImprimir(f"{wTotCedulas} Registro(s) a consultar",5)       
        # Recorremos de manera agrupada
        for juzgado in wArrDatosGenerales: 
            try:
                wMes = ""
                # Recorremos segun el grupo
                contJuzg = 0
                for datos in wArrDatosGenerales[juzgado]:
                    try:  
                        app_juzgado.fmLimpiandoCarpeta( app_config.wRutaDescPdf )
                        app_juzgado.fmLimpiandoCarpeta( app_config.wRutaDescPdfFin )
                        app_juzgado.fmLimpiandoCarpeta( app_config.wRutaDescPdfFinV2 )
                        
                        app_general.fnImprimir(f"[{str(wCont).zfill(len(str(wTotCedulas)))} / {wTotCedulas}] {juzgado} - Nro Radicado : {datos['NumeroRadicacion']}",7)
                                           
                        wMesDiv         = str(int(datos["FechaIniciaTermino"].split('-')[1])) #{Nro Mes} 
                        wCiuJuzgado     = juzgado.replace('-'+juzgado.split('-')[-1],'')      #juzgado[0:10]  #{Ciudad}-{Nro Juzgado}
                        wValorJuzgado   = app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado)
                        if wValorJuzgado is not None:
                            wSeleccionarMes = True if wValorJuzgado.xpath_pest != '' else False
                        
                            if wValorJuzgado.xpath_tab == "":
                                app_general.fnImprimir(f"No se encontro información para el juzgado.",9)
                                continue
                            #fin if 
                        else:
                            app_general.fnImprimir(f"Juzgado en mantenimiento revisar.",9)
                            continue
                        #fin if  
                        
                        
                        # if wCiuJuzgado not in (  'EE-6-20-387-287','EE-6-20-387-304','EE-6-20-387-306','EE-6-20-387-307','EE-6-20-387-700','EE-6-19-367-112','EE-6-19-367-113','EE-4-7-89-115','EE-6-20-398-116','EE-6-20-398-117','EE-6-20-398-118','EE-6-20-398-119','EE-6-19-367-110','EE-6-19-367-120','EE-6-19-371-131','EE-6-19-371-130','EE-6-19-371-132','EE-6-19-371-133','EE-6-19-371-134','EE-6-19-371-135','EE-6-19-371-136','EE-6-19-371-137','EE-6-19-371-138','EE-6-19-355-140','EE-6-19-355-141','EE-6-19-355-143','EE-6-19-355-144','EE-6-19-355-145','EE-6-19-355-150','EE-6-19-355-151','EE-6-19-355-152','EE-6-19-355-153','EE-6-19-355-154','EE-6-19-382-175','EE-6-19-382-177','EE-6-19-382-179','EE-6-19-382-181','EE-6-19-382-182','EE-6-19-382-184','EE-6-19-382-185','EE-6-19-382-187','EE-6-19-382-188','EE-6-20-387-290','EE-6-20-387-305','EE-4-7-78-352','EE-6-20-387-302','EE-4-7-78-348','EE-4-7-78-349','EE-4-7-78-360','EE-4-7-78-361','EE-4-7-78-362','EE-6-20-387-698','EE-4-7-78-321','EE-6-20-387-274','EE-7-24-498-266','EE-7-24-498-265','EE-7-24-498-89','EE-7-24-498-267','EE-7-24-498-90','EE-7-24-498-269','EE-7-24-498-270','EE-7-24-498-271','EE-7-24-498-272','EE-4-7-78-326','EE-4-7-78-94','EE-4-7-78-329','EE-4-7-78-96','EE-4-7-78-97','EE-7-24-498-258','EE-7-24-498-259','EE-7-24-498-260','EE-7-24-498-261','EE-7-24-498-262','EE-7-24-498-255','EE-7-24-498-256','EE-7-24-498-263','EE-7-24-498-264','EE-6-19-356-3','EE-7-24-498-273','EE-6-19-356-1','EE-6-19-356-8','EE-6-19-356-9','EE-6-19-356-10','EE-6-19-356-11','EE-6-19-356-18','EE-6-19-356-21','EE-6-19-356-28','EE-6-19-356-29','EE-6-19-356-30','EE-6-19-356-33','EE-6-19-356-34','EE-6-19-356-37','EE-6-19-356-38','EE-6-19-356-39','EE-6-19-356-40','EE-6-19-356-41','EE-6-19-356-42','EE-6-19-356-43','EE-6-19-356-44','EE-6-19-356-45','EE-6-19-356-46','EE-6-19-356-48','EE-6-19-356-49','EE-6-19-356-51','EE-6-19-356-56','EE-6-19-356-59','EE-6-19-356-62','EE-6-19-356-63','EE-6-19-356-64','EE-6-19-356-65','EE-6-19-356-68','EE-6-19-356-69','EE-6-19-356-70','EE-6-19-356-71','EE-6-19-356-72','EE-6-19-356-60','EE-6-20-387-310','EE-6-19-356-83','EE-6-20-387-312','EE-6-20-387-314','EE-6-20-387-315','EE-6-20-387-316','EE-4-7-78-323','EE-6-20-387-268','EE-4-7-78-355','EE-4-7-78-356','EE-4-7-78-347','EE-6-20-387-297','EE-4-7-78-344','EE-6-20-387-295','EE-4-7-78-345','EE-4-7-78-343','EE-6-20-387-291','EE-6-19-357-251','EE-6-19-357-252','EE-6-19-367-246','EE-6-19-367-247','EE-6-19-367-243','EE-6-19-367-241','EE-6-19-382-206','EE-6-19-380-160','EE-6-19-382-201','EE-6-19-382-180','EE-6-19-367-156','EE-6-19-367-126','EE-6-19-367-127','EE-6-19-367-128','EE-4-7-89-124','EE-4-7-89-125','EE-6-20-387-283','EE-6-20-387-108','EE-6-20-387-109','EE-6-19-356-86','EE-6-19-356-87','EE-6-19-356-78'  ):
                        #     continue
                        # #fin if
                                                
                        # Proceso de Inicio 
                        driver, continuar = app_juzgado.fnProcesoPaginaInicio( driver, app_juzgado.datos_juzgados.juzgadosJSON.get(juzgado).url )
                        if continuar: continue
                          
                        if '502 Bad Gateway' in driver.page_source:
                            app_general.fnImprimir(f"Ocurrio un incoveniente con la pagina. error 502",9)
                            app_log.error( f"ERROR 502 Bad Gateway." )
                            
                            driver.quit()
                            driver = None
                            continue
                        #fin fin 
                        
                        ### PROCESO 01
                        if wCiuJuzgado == 'EE-6-20-387-299':   # JUZGADO 035 DE PEQUEÑAS CAUSAS Y COMPETENCIA MÚLTIPLE DE BOGOTÁ
                            app_juzgado.fnProcesos( 1, juzgado, ['td[2]', 'ESTADO-69-3|PROVIDENCIAS-01-4', 'td[1]', '/', 1, 0, True, True, 1 ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 02
                        elif wCiuJuzgado == 'EE-4-7-78-327': # JUZGADO 012 CIVIL DEL CIRCUITO DE BOGOTÁ
                            app_juzgado.fnProcesos( 2, juzgado, ['td[2]' , True, 'td[3]'], wSeleccionarMes, driver, datos, wMesDiv, wMes )  
                        
                        ### PROCESO 03
                        elif wCiuJuzgado == 'EE-4-7-78-91':  # JUZGADO 001 CIVIL DEL CIRCUITO DE BOGOTÁ
                            app_juzgado.fnProcesos( 3, juzgado, ['td[1]','td[8]', True, False,True], wSeleccionarMes, driver, datos, wMesDiv, wMes )  

                        ### PROCESO 04
                        elif wCiuJuzgado == 'EE-6-20-387-308': # JUZGADO 044 DE PEQUEÑAS CAUSAS Y COMPETENCIA MÚLTIPLE DE BOGOTÁ
                            app_juzgado.fnProcesos( 4, juzgado, ['td[2]','td[1]-00-01', True, -1 ], wSeleccionarMes, driver, datos, wMesDiv, wMes )

                        ### PROCESO 05
                        elif wCiuJuzgado == 'EE-6-19-356-5':  #JUZGADO 005 CIVIL MUNICIPAL DE BOGOTÁ
                                app_juzgado.fnProcesos( 5, juzgado, ['td[2]', 'No. ESTADO-00|PROVIDENCIAS-01', True ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 06
                        elif wCiuJuzgado == 'EE-6-19-356-16': #JUZGADO 016 CIVIL MUNICIPAL DE BOGOTÁ
                            app_juzgado.fnProcesos( 6, juzgado, ['td[3]', datos["NumeroRadicacion"],  -1, True,  ], False, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 07
                        elif wCiuJuzgado == 'EE-4-7-78-335': # JUZGADO 021 CIVIL DEL CIRCUITO DE BOGOTÁ
                            app_juzgado.fnProcesos( 7, juzgado, ['td[2]', True, 'td[4]' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )            
                        
                        ### PROCESO 08
                        
                        ### PROCESO 09
                        elif wCiuJuzgado == 'EE-6-19-352-213': # JUZGADO 005 CIVIL MUNICIPAL DE MEDELLÍN ( ESTADO -- ) Obs: NO CUENTA CON ESTADO:
                            app_juzgado.fnProcesos( 9, juzgado, ['td[1]', True, 'td[1]' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 10
                        elif wCiuJuzgado == 'EE-6-19-356-53': #JUZGADO 053 CIVIL MUNICIPAL DE BOGOTÁ
                            app_juzgado.fnProcesos( 10, juzgado, ['td[2]','td[3]', 1, True, False, 'td[1]' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 11
                        elif wCiuJuzgado == 'EE-4-7-78-99':  # JUZGADO 043 CIVIL DEL CIRCUITO DE BOGOTÁ
                            app_juzgado.fnProcesos( 11, juzgado, ['td[4]' , True, 'td[3]'], wSeleccionarMes, driver, datos, wMesDiv, wMes )
            
                        ### PROCESO 12
                        elif wCiuJuzgado == 'EE-4-7-78-353': #JUZGADO 044 CIVIL DEL CIRCUITO DE BOGOTÁ
                            app_juzgado.fnProcesos( 12, juzgado, [ True, 'ESTADO-01' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )                        
                        
                        ### PROCESO 13
                        elif wCiuJuzgado == 'EE-6-19-356-14': #JUZGADO 014 CIVIL MUNICIPAL DE BOGOTÁ
                            app_juzgado.fnProcesos( 13, juzgado, ['td[2]', True, '01'], wSeleccionarMes, driver, datos, wMesDiv, wMes )  
                        
                        ### PROCESO 14
                        elif wCiuJuzgado == 'EE-6-20-387-106': # JUZGADO 004 DE PEQUEÑAS CAUSAS Y COMPETENCIA MÚLTIPLE DE BOGOTÁ
                            app_juzgado.fnProcesos( 14, juzgado, [ True, 'ESTADO-28' ], wSeleccionarMes, driver, datos, wMesDiv, wMes ) 
                        
                        ### PROCESO 15
                        elif wCiuJuzgado == 'EE-6-20-387-275': # JUZGADO 010 DE PEQUEÑAS CAUSAS Y COMPETENCIA MÚLTIPLE DE BOGOTÁ
                            app_juzgado.fnProcesos( 15, juzgado, [ True, 'ESTADO-23' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                                
                        ### PROCESO 16
                        elif wCiuJuzgado == 'EE-6-19-352-211': # JUZGADO 003 CIVIL MUNICIPAL DE MEDELLÍN ( ESTADO -- ) Obs:
                            if datos['Anio'] == '2021':
                                app_juzgado.fnProcesos( 16, juzgado, [ True, 'ESTADO-23' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 17
                        elif wCiuJuzgado == 'EE-6-19-352-212': # JUZGADO 004 CIVIL MUNICIPAL DE MEDELLÍN ( ESTADO -- ) Obs:
                            if datos['Anio'] in ('2022','2021'):
                                app_juzgado.fnProcesos( 17, juzgado, [ True, 'ESTADO-23' ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 18
                                            
                        ### PROCESO 19
                        elif wCiuJuzgado == 'EE-6-19-352-234': # JUZGADO 026 CIVIL MUNICIPAL DE MEDELLÍN ( ESTADO -- ) Obs:
                            if datos['Anio'] == '2023':
                                app_juzgado.fnProcesos( 19, juzgado, [ True, 'ESTADO-23' ], wSeleccionarMes, driver, datos, wMesDiv, wMes ) 
                        
                        ### PROCESO 20
                        elif wCiuJuzgado == 'EE-6-19-352-236': # JUZGADO 028 CIVIL MUNICIPAL DE MEDELLÍN ( ESTADO -- ) Obs:
                            app_juzgado.fnProcesos( 20, juzgado, ['td[3]','td[3]', True], wSeleccionarMes, driver, datos, wMesDiv, wMes ) 
                        
                        ### PROCESO 21
                        elif wCiuJuzgado == 'EE-4-7-89-123': # JUZGADO 001 CIVIL DEL CIRCUITO DE ZIPAQUIRÁ
                            meses_dict = { 'enero': (2, 1), 'febrero': (2, 2), 'marzo': (2, 3), 'abril': (4, 1), 'mayo': (4, 2), 'junio': (4, 3), 'julio': (6, 1), 'agosto': (6, 2), 'septiembre': (6, 3), 'octubre': (8, 1), 'noviembre': (8, 2), 'diciembre': (8, 3) }
                            app_juzgado.fnProcesos( 21, juzgado, [ True, 'ESTADO-08', meses_dict ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 22
                        elif wCiuJuzgado == 'EE-6-19-356-14': #JUZGADO 014 CIVIL MUNICIPAL DE BOGOTÁ
                            if datos['Anio'] == '2024':
                                app_juzgado.fnProcesos( 22, juzgado, ['td[2]', True, 1 ], wSeleccionarMes, driver, datos, wMesDiv, wMes )  
                        
                        ### PROCESO 23
                        elif wCiuJuzgado == 'EE-6-20-387-289': # JUZGADO 024 DE PEQUEÑAS CAUSAS Y COMPETENCIA MÚLTIPLE DE BOGOTÁ
                            if datos['Anio'] == '2024':
                                meses_dict = { 'enero': (4, 2), 'febrero': (4, 10), 'marzo': (4, 18), 'abril': (13, 2), 'mayo': (13, 10), 'junio': (13, 18), 'julio': (22, 2), 'agosto': (22, 10), 'septiembre': (22, 18), 'octubre': (31, 2), 'noviembre': (31, 10), 'diciembre': (31, 18) }
                                app_juzgado.fnProcesos( 23, juzgado, [ True, 'ESTADO-41', meses_dict ], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                        ### PROCESO 24
                        
                        ### PROCESO 25
                        elif wCiuJuzgado == 'EE-4-7-78-334': # JUZGADO 020 CIVIL DEL CIRCUITO DE BOGOTÁ
                                app_juzgado.fnProcesos( 25, juzgado, [True], wSeleccionarMes, driver, datos, wMesDiv, wMes )
                        
                    
                    except: 
                        app_general.fnImprimir(f"ERROR: Ocurrio un inconveniente en el recorrido secundario, favor de revisar el log.")
                        app_log.error( f"ERROR en el for secundario - {juzgado} - {datos['NumeroRadicacion']} - MSJ ERROR: {sys.exc_info()[1]}" )
                        
                        if driver != None:
                            driver.quit()
                            driver = None
                        #fin if
                        pass
                    finally:
                        wMes = datos['Mes']
                        wCont+=1
                        contJuzg+=1
                    #fin try
                #fin for
            except:
                app_general.fnImprimir(f"ERROR: Ocurrio un inconveniente en el recorrido principal, favor de revisar el log.")
                app_log.error( f"ERROR en el for principal: {sys.exc_info()[1]}" )
                pass
            finally: 
                #Cerramos el div
                if driver != None:
                    driver.quit()
                    driver = None
                #fin if
            #fin try
        #fin for
    except:
        app_general.fnImprimir(f"ERROR: Ocurrio un inconveniente en la función fnProcesarDatos, favor de revisar el log.")
        app_log.error( f"ERROR en la funcion fnProcesarDatos: {sys.exc_info()[1]}" )
        pass
    finally:
        if driver != None:
            driver.quit()
            driver = None
        #fin if
    #fin try
    
    return driver
#fnProcesarDatos
  
if __name__ == "__main__":
    os.system('cls')
    
    app_apiModel = ApiModel()
    app_juzgado  = JuzgadoBase() 
    app_general  = app_juzgado.app_general
    app_config   = app_juzgado.app_config
    app_log      = app_juzgado.app_log
    
    while True:
        # Variables
        driver = None 
        
        try:
            os.system('cls')
            app_general.fnImprimirTitulo(f"Proceso [::JUZGADO MUNICIPAL::] ejecutandose {app_general.fnConvertirFechaHora(app_general.fnConfigFecha('FHA'),'-','/')}")
            app_log.info(f"Proceso INICIO [::JUZGADO MUNICIPAL::].")
            
            app_apiModel.fnEjecutarApiPost('BusquedaRadicacion','ConsultaRamaJudicial')
            objDatos = app_apiModel.fnRetornarData()
            
            if objDatos['Code'] == 200:
                if len(objDatos['Data']) > 0: 
                    
                    driver = fnProcesarDatos( driver, objDatos['Data'], app_apiModel, app_juzgado, app_general, app_config, app_log )                    
                    time.sleep(1)
                else:
                    app_general.fnImprimir(f"RPTA: No se encontraron registros")
                #fin if 
            else:
                app_general.fnImprimir(f"RPTA: Ocurrio un incoveniente con consultar el Api, favor de revisar el log.")
                app_log.error(objDatos['Message'])
            #fin if 
             
            
        except:
            app_general.fnImprimir(f"ERROR: Ocurrio un inconveniente en el proceso, favor de revisar el log.")
            app_log.error( f"ERROR: {sys.exc_info()[1]}" )
            pass
        finally:
            if driver != None:
                driver.quit()
                driver == None
            #fin if
        #fin try
      
        app_general.fnSaltoLinea()
        app_general.fnImprimir("Este proceso se ejecutará en 1 min.")
        time.sleep(60 )
    #fin while
#fin if