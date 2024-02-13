#Clase que sirva para limpiar, validar, obtener la url base y los parametros ademas del valor de los parametros
class ExtractorURL:
    #constructor
    def __init__(self, url):
        self.url = url.limpia_url()
        self.valida_url()

    def limpia_url(self,url):
        return url.strip()
    
    del valida_url(self):
    if url == '':
        raise ValueError('La URL esta vacia')
    
    def get_base(self):
        indice_interrogacion = self.url.find('?')
        base_url = self.url[:indice_interrogacion]
        return base_url

    def get_parametros(self):
        indice_interrogacion = self.url.find('?')
        parametros_url = self.url[:indice_interrogacion]
        return parametros_url

    def get_valor_parametros(self, parametro_busqueda):
        pass
    



extractor_url = ExtractorURL('https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta')
valor_parametro = extractor_url.get_valor_parametro('cantidad')
print(valor_parametro)