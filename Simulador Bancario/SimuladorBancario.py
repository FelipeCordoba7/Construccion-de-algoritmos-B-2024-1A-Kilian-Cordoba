__autor__="Kilian Felipe Cordoba Rivera"
__license__= "GPL"
__version__= "1.0.0"
__email__="kilian.cordoba@campusucc.edu.co"

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    #Aqui inicia mi clase
    
    ''' -------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------'''
    
    __nombre= ""
    __cedula = ""
    
    
    __cuentaCorriente= CuentaCorriente()
    __cuentaAhorros=CuentaAhorros()
    __cdt= CDT()
    
    __mesActual= 0
    
    '''#---------------------------------------------------------------------------
    #Metodos 
    ---------------------------------------------------------------------------#'''
        
    __method__="ConsignarCuentaCorriente"
    __params__="Monto"
    __returns__="Nada"
    __description__="Este metodo permite consignar a la cunet a corriente"
    
    def ConsignarCuentaCorriente(self, monto):
        #Aqui inicia mi metodo
        self._cuentaCorriente.ConsignarValor(monto)
        
        
    __method__="CalcularSaldoTotal"
    __params__="Ninguno"
    __returns__="Retorna saldo total"
    __description__="Este metodo suma el saldo de todas las cuentas"
    
    def CalcularSaldoTotal(self):
        #Aqui inicia mi metodo
        #forma1
        total= self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__="PasarAhorrosCorriente"
    __params__="Ninguno"
    __returns__="Ninguno"
    __description__="Este metodo transfiere el saldo de ahorros a corriente"
    def PasarAhorrosCorriente(self):
        #Aqui inicia mi metodo
        #Pasar ahorros a corriente
        saldoTemporal=self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)

    
    __method__="Ahorro"
    __params__="monto"
    __returns__="Ninguno"
    __descriptions__="Pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parametro"
    def Ahorro(self, monto):
        #Aqui inicia mi metodo
        self.__cuentaCorriente.RetirarValor(monto)
        self.__cuentaAhorros.ConsignarValor(monto)



    __method__="retirarAhorro"
    __params__="monto"
    __returns__="Ninguno"
    __descriptions__="Retira un valor dado de la cuenta de ahorros"
    def retirarAhorro(self, monto):
        #Aqui inicia mi metodo
        self.__cuentaAhorros.RetirarValor(monto)


    __method__="darSaldoCorriente"
    __params__="Ninguno"
    __returns__="Devuelve el saldo de la cuenta corriente"
    __descriptions__="Retorna el saldo que hay en la cuenta corriente"
    def darSaldoCorriente(self):
       #Aqui inicia mi metodo
       return self.__cuentaCorriente.DarSaldo()



    __method__="RetirarTodo"
    __params__="Ninguno"
    __returns__="retiro total"
    __descriptions__="Retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros"
    def retirarTodo(self):
        #Aqui inicia mi metodo
        self.__cuentaCorriente.RetirarValor(self.__cuentaCorriente.DarSaldo())
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldo())
    



    __method__="DuplicarAhorro"
    __params__="monto"
    __returns__="Ninguno"
    __descriptions__="Duplica la cantidad de dinero que hay en la cuenta de ahorros"
    def duplicarAhorro(self):
        #Aqui inicia mi metodo
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldo())
            
        
    
    
    
    
    
    