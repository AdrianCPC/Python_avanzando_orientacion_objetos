edades=[15,18,59,71]
type(edades)

edades.append(35)
edades

#List comprehension
edades_proximo_year = []
edades_proximo_year = [edad + 1 for edad in edades]
edades_proximo_year

mayores_de_edad_pa = [edad + 1 for edad in edades if edad > 21]
mayores_de_edad_pa

#Problemas mutalidad listas
def analisis_listas(lista=None):
    print(id(lista))
    if lista == None:
        lista = list()
        print(id(lista))
    print(len(lista))
    lista.append(13)
    return lista

edades = [16,19,60,72,36,19,46,36]

analisis_listas()


#Creacion de la clase cuenta bancaria
class CuentaCorriente:
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0
        
    def deposito(self, valor):
        self.saldo += valor
        
    def __str__(self):
        return f'>>> Código: {self.codigo} ---- Saldo: {self.saldo}<<<'
    
#creacion cuentas personales
cuenta_alvaro = CuentaCorriente(16)
cuenta_alvaro.deposito(500.0)
cuenta_stef = CuentaCorriente(17)
cuenta_stef.deposito(1000.0)

#aplicando por medio de una lista las cuentas 
cuentas = [cuenta_alvaro,cuenta_stef]

for cuenta in cuentas:
    print(cuenta)