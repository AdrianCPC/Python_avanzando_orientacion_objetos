import re

#Clase que sirva para limpiar, validar, obtener la url base y los parametros ademas del valor de los parametros
class ExtractorURL:
    #constructor
    def __init__(self, url):
        self.url = self.limpia_url(url)
        self.valida_url()

        #Limpiar URL
    def limpia_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    #Validar URL
    def valida_url(self):
        if not self.url:
            raise ValueError('La URL esta vacia')
        
        patron_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.mx)?/cambio')
        match = patron_url.match(self.url)
        if not match:
            print('La url no es invalida')
    
    #Obtencion URL base
    def get_base(self):
        indice_interrogacion = self.url.find('?')
        base_url = self.url[:indice_interrogacion]
        return base_url
    
    #Obtencion de parametros
    def get_parametros(self):
        indice_interrogacion = self.url.find('?')
        parametros_url = self.url[:indice_interrogacion]
        return parametros_url

    def get_valor_parametro(self, parametro_busqueda):
        parametro_busqueda = parametro_busqueda
        indice_parametro = self.get_parametros().find(parametro_busqueda)
        indice_valor = indice_parametro + len(parametro_busqueda) + 1
        indice_and = self.get_parametros().find('&', indice_valor)
        if indice_and == -1:
            valor = self.get_parametros()[indice_valor]
        else:
            valor = self.get_parametros()[indice_valor:indice_and]

        return valor
'''
Ejemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.mx/cambio
    www.bytebank.com/cambio
    www.bytebank.com.mx/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.mx/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.mx/cambio

Ejemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.noexiste/cambio
    ht:bytebank.noexiste/cambio

'''

#URL = 'https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta'

extractor_url = ExtractorURL('https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta')
#valor_parametro = extractor_url.get_valor_parametro('cantidad')
#print(valor_parametro)



