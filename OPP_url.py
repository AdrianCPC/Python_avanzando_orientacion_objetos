#Clase que sirva para limpiar, validar, obtener la url base y los parametros ademas del valor de los parametros
class ExtractorURL:
    #constructor
    def __init__(self, url):
        self.url = self.limpia_url(url)
        self.valida_url()

        #Limpiar URL
    def limpia_url(self,url):
        return url.strip()
    
    #Validar URL
    def valida_url(self):
        if self.url == '':
            raise ValueError('La URL esta vacia')
    
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

     



extractor_url = ExtractorURL('https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta')
valor_parametro = extractor_url.get_valor_parametro('cantidad')
print(valor_parametro)