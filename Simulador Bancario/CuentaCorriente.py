__autor__="Kilian Felipe Cordoba Rivera"
__license__= "GPL"
__version__= "1.0.0"
__email__="kilian.cordoba@campusucc.edu.co"

class CuentaCorriente: 
    ''' -------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------'''
    
    _saldo=0
    
    '''#---------------------------------------------------------------------------
    #Metodos 
    ---------------------------------------------------------------------------#'''
        
    __method__="ConsignarValor"
    __params__="monto"
    __returns__="Nada"
    __description__="Este metodo permite consignar un monto a la cuenta"
    def ConsignarValor(self, monto):
        #Aqui inicia el metodo
        #self._cuentaCorriente.saldo=self._cuentaCorriente.saldo+monto #esta manera es erronea por vulnerabilidades
        self._saldo=self._saldo+monto
        
        
    __method__="DarSaldo"
    __params__="Ninguno"
    __returns__="Saldo"
    __description__="Este metodo retorna el saldo"
    
    def DarSaldo(self):
        #Aqui inicia el metodo
        return self._saldo
    
    __method__="RetirarValor"
    __params__="monto"
    __returns__="Nada"
    __description__="Este metodo retira un monto a la cuenta"
    
    def RetirarValor(self, monto):
        self._saldo=self._saldo-monto