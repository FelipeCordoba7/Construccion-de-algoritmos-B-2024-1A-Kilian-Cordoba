__autor__="Kilian Felipe Cordoba Rivera"
__license__= "GPL"
__version__= "1.0.0"
__email__="kilian.cordoba@campusucc.edu.co"

class fecha:
    '''#---------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------#'''
    
    dia = 0
    mes = 0
    año = 0
    '''#---------------------------------------------------------------------------
    #Metodos 
    ---------------------------------------------------------------------------#'''
    
    __method__="DarDia"
    __params__="Ninguno"
    __returns__="Dia"
    __description__="Devuelve el dia de la clase"
    
    def DarDia(self):
        #Aqui inicia el metodo
        return self.dia
    
        
    __method__="DarMes"
    __params__="Ninguno"
    __returns__="Mes"
    __description__="Devuelve el Mes de la clase"
    
    def DarMes(self):
        #Aqui inicia el metodo
        return self.mes


    __method__="DarAnio"
    __params__="Ninguno"
    __returns__="Anio"
    __description__="Devuelve el anio de la clase"
    
    def DarAnio(self):
        #Aqui inicia el metodo
        return self.anio
    
    __method__ = 'DarFecha'
    __params__ = "ninguno"
    __returns__ = "Fecha de la clase"
    __Description__ = "Devuelve la fecha de la clase"
    
    def DarFecha(self):
        #Aqui inicia el metodo
        return self.dia+'/'+self.mes+'/'+self.anio
    
    