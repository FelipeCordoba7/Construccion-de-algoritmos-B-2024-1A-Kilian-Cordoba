__autor__="Kilian Felipe Cordoba Rivera"
__license__= "GPL"
__version__= "1.0.0"
__email__="kilian.cordoba@campusucc.edu.co"

''' -------------------------------------------------------------------------
#Importacion
 ---------------------------------------------------------------------------'''
 
from Fecha import Fecha

class Empleado:
    #Aqui inicia mi clase
    
    ''' -------------------------------------------------------------------------
    #Atributos
    ---------------------------------------------------------------------------'''
    
    nombre = ""
    apellido = ""
    salario = 0
    
    '''#-------------------------------------------------------------------------
    # 1 Masculino y 2 Femenino  
    ---------------------------------------------------------------------------#'''
    Sexo = 0
    
    ''' -------------------------------------------------------------------------
    #Asociaciones 
    ---------------------------------------------------------------------------'''
    
    fechaNacimiento = Fecha()
    fechaIngreso =Fecha()
    
    '''#---------------------------------------------------------------------------
    #Metodos 
    ---------------------------------------------------------------------------#'''
        
    __method__="CambiarSalario"
    __params__="nuevoSalario"
    __returns__="Nada"
    __description__="Este metodo permite cambiar el salario del empleado por uno nuevo"
    
    def CambiarSalario(self,nuevoSalario):  
        #Aqui inicia el metodo
        self.salario=nuevoSalario
    
    __method__="DarSalario"
    __params__="Ninguno"
    __returns__="Salario empleado"
    __description__="Devuelve el salario del empleado"
    
    
    def DarSalario(self):
        #Aqui inicia el metodo
        return self.salario

    __method__="AumentoSalario"
    __params__="aumento"
    __returns__="Ninguno"
    __description__="Permite aumentar el salario de un valor ingresado por el usuario"
    
    def Aumentosalario(self,aumento):
        #Aqui inicia el metodo
        self.salario = self.salario+aumento
        
    __method__="CalcularSalarioAnual"
    __params__="Ninguno"
    __returns__="salario anual"
    __description__="Permite calcular el salario anual del empleado"
    
    def CalcularSalarioAnual(self):
        #Aqui inicia el metodo
        return self.salario*12
    
    __method__="CalcularImpuestoSalarioAnual"
    __params__="Ninguno"
    __returns__="Impuesto del salario anual"
    __description__="Permite calcular el impuesto  del salario anual del empleado"
    
    def CalcularImpuestoSalarioAnual(self):
     #Aqui inicia el metodo 
     SalarioAnual= self.CalcularSalarioAnual()
     return SalarioAnual*0.19       
 
 

    __method__="CalcularImpuestoSalario"
    __params__="Ninguno"
    __returns__="Impuesto del salario mensual"
    __description__="Permite calcular el impuesto del salario del empleado"
    
    def CalcularImpuestoSalario(self):
        #Aqui inicia el metodo
        return self.DarSalario()*0.19   
    
    __method__="DarFechaIngreso"
    __params__="Ninguno"
    __returns__="Fecha de ingreso"
    __description__="Muestra la fecha de ingreso del empleado"
    
    def DarFechaIngreso(self):
        #Aqui inicia el metodo
        return self.fechaIngreso.DarFecha()
    
    __method__="DarFechaNacimiento"
    __params__="Ninguno"
    __returns__="Fecha de nacimiento"
    __description__="Muestra la fecha de nacimiento del empleado"
    
    def DarFechaNacimiento(self):
        #Aqui inicia el metodo
        return "Tu fecha de nacimiento es"* self.fechaNacimiento.DarFecha()
      
    
    
    
