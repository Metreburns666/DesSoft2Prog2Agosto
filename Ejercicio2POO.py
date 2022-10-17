import os
os.system("cls")
class Cuenta: 


    def __init__ (self, titular, cantidad):  
        self.__titular = titular or "" 
        self.__cantidad = cantidad or ""
    
    
    @property
    def getTitular(self):
        return self.__titular
    def getCantidad(self):
        return self.__cantidad

    def titular(self,titular):
        self.__titular = titular
    
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def __str__(self): 
        return f"Datos ingresados: \nNombre del titular: {self.__titular} \nCantidad: ${self.__cantidad} \n"
    
    def ingresar(self):
        while True:
            try:
                depo=float(input("Indique el monto de dinero a depositar: "))     
            except ValueError:
                print("Dato erroneo, por favor escribe un número.")
                continue
            else:
                break
        print(f"Ud va a depositar en su cuenta un monto total de $ {depo}")
        self.__cantidad = self.__cantidad + depo
        print (f"En su cuenta ahora tiene $ {self.__cantidad}")
    def retirar (self):
        while True:
            try:
                retiro=float(input("Ingrese la cantidad de dinero a retirar: "))     
            except ValueError:
                print("Dato erroneo, por favor escribe un numero.")
                continue
            else:
                break
        print(f"Ud ha retirado de su cuenta la suma de $ {retiro}")
        self.__cantidad = self.__cantidad - retiro
        print (f"En su cuenta ahora tiene $ {self.__cantidad}")
finTitular = False
while (finTitular != True):
    titular = input("Ingrese nombre y apellido del titular de la cuenta: ")   
    list(titular)
    if (titular.isnumeric()):
        print("Dato erroneo, Ud ingreso un numero")
        finTitular = False
    elif(len(titular)<2):
        print("Ingrese una opcion valida")
        finTitular = False
    else:
        finTitular = True
while True:
    try:
        cantidad = float(input("Ingrese fondos disponibles: "))
    except ValueError:
        print("Debe escribir un número")
        continue
    if cantidad < 0:
        pass
    else:    
        break

persona1 = Cuenta(titular, cantidad)
print(persona1)
persona1.ingresar()
persona1.retirar()
