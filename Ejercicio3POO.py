import os
os.system("cls")

class Cuenta: 

    def __init__ (self, titular, cantidad):  
        self.titular = titular or "" 
        self.cantidad = cantidad or ""
    
    @property
    def getTitular(self):
        return self.titular
    def getCantidad(self):
        return self.cantidad

    def titular(self,titular):
        self.titular = titular
    def cantidad(self,cantidad):
        self.cantidad = cantidad
    def mostrar(self):
        print(f"Datos ingresados: \nNombre del titular: {self.titular} \nCantidad: ${self.cantidad} \n")
    

class CuentaJoven (Cuenta):
    def __init__ (self, titular, cantidad, edad, bonificacion):
        super().__init__(titular,cantidad)
        self.edad = edad
        self.bonificacion = bonificacion

    def getEdad (self):
        return self.edad
    def getBonificacion(self):
        return self.bonificacion

    def setEdad (self, edad):
        self.edad = edad
    def setBonificacion(self,bonificacion):
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if self.edad >=18 and self.edad <=25:            
            return True
        else:    
            return False
    
    def mostrar(self):
        super().mostrar()
        if self.esTitularValido() == False:
            print("Su edad no cumple con los requisitos para tener una Cuenta Joven")
            print("Su cuenta no tiene bonificaciones")
            print("No se encuentra habilitado para retirar dinero de  Cuenta Joven")
        else:
            print("Bienvenido a Cuenta Joven")
            print(f"Su Cuenta Joven tiene una bonificacion de {self.bonificacion} %")
    
    
    def acreditacion(self):
        if self.esTitularValido() == True:
            acreditacion = round(((cantidad) * self.bonificacion/100),2) 
            print(f"Su bonificacion representa un total de $ {acreditacion}")

    def retirar (self):
        if self.esTitularValido() == True: 
            while True:
                try:
                    retiro = float(input("Ingrese la cantidad de dinero a retirar: "))     
                except ValueError:
                    print("Dato erroneo, por favor escribe un numero.")
                    continue
                else:
                    break
            print(f"Ud ha retirado de su cuenta la suma de $ {retiro}")
            self.cantidad = self.cantidad - retiro
            print (f"En su cuenta ahora tiene $ {self.cantidad}")
        
finTitular = False
while (finTitular != True):
    titular =input("Por favor ingrese su nombre completo: ")
    if titular == "":
        pass    
    list(titular)
    if (titular.isnumeric()):
        print("Dato incorrecto, Usted ha ingresado un número")
        finTitular = False
    elif(len(titular)<2):
        print("Ingrese una opcion válida")
        finTitular = False
    else:
        finTitular = True
while True:
    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Debe ingresar un número y que no sea decimal")
        continue
    if edad < 0:
        print("Debe ingresar un número positivo.")
        continue
    if edad >=100:
        print ("Debe ingresar una edad menor")
        continue
    else:    
        break
while True:
    try:
        cantidad = float(input("Ingrese montos disponibles: "))
    except ValueError:
        print("Por favor ingresar un número")
        continue
    if cantidad < 0:
        pass
    else:    
        break
while True:
    try:
        bonificacion = float(input("Por favor ingrese el porcentaje de bonificacion que recibe: "))
    except ValueError:
        print("Por favor ingrese un número")
        continue
    if bonificacion < 0:
        print("Debe ingresar un porcentaje positivo")
    else:    
        break

personaJoven = CuentaJoven(titular,cantidad,edad,bonificacion)
personaJoven.esTitularValido()
personaJoven.mostrar()
personaJoven.acreditacion()
personaJoven.retirar()
