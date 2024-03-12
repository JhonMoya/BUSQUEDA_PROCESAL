from appGenerales import AppGenerales
import requests

class ApiModel:
    def __init__(self):
        self.app_general = AppGenerales()
        self.app_config  = self.app_general.appConfig
        
        self.data = {
             'Success'  : True
            ,'Message' : ''
            ,'Code'    : 202
        }
    #__init__
        
    def fnEjecutarApiPost(self, nombre_api, funcion_api, params_post={}, retorna_json = True, msj_personalizado = 'Se ejecutó exitosamente' ):
        """Ejecutamos el request metodo POST"""
        try:
            self.data = {'Success': True, 'Message' : msj_personalizado }
            data_post = requests.post(url = (self.app_config.wRutaApi +nombre_api+'/'+funcion_api), data = params_post, headers= {'Content-Type': 'application/json;  charset=utf-8'} )
            if data_post.status_code == 200:
                self.data = data_post.json()
            else:
                self.data['Success'] = False
                self.data['Message'] = data_post.text
                self.data['Code']    = data_post.status_code 
            #fin if 
        except requests.HTTPError as e:
            self.data = { 'Success': False, 'Message' : e }
        #fin try
        
        return self.data
    #fnEjecutarApiPost
        
    def fnEjecutarApiGet(self, nombre_api, funcion_api, pamars_get = {}, retornar_json = True, msj_personalizado = 'Se ejecutó exitosamente' ):
        """Ejecutamos el request metodo GET""" 
        try:
            data_get = requests.get(url = (self.app_config.wRutaApi + nombre_api+'/'+funcion_api), params = pamars_get)
            self.data = data_get.json() if retornar_json else {'success': True, 'message' : msj_personalizado }
        except requests.HTTPError as e:
            self.data = { 'success': False, 'message' : e }
        #fin try 
    #fnEjecutarApiGet
     
    def fnRetornarData(self):
        return self.data
    #fnRetornarData
    