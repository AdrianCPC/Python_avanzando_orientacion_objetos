url ='www.bytebank.com/cambio?monedaOrigen=usd'
base_url = url[0:23]
parametros_url = url[24:41]

print(base_url, parametros_url)

url2 = 'https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta'
url2.find('?')

indice_interrogacion = url2.find('?')
base_url2 =url2[:indice_interrogacion]
parametros_url2 = url2[indice_interrogacion + 1:]
print(base_url2)
print(parametros_url2)

parametro_busqueda = 'operacion'
indice_parametro = parametros_url2.find(parametro_busqueda)
indice_valor = indice_parametro + len(parametro_busqueda) + 1

valor = parametros_url2[indice_valor:]
print(valor)