class persona:
    def __init__(self,nombre,edad,DNI):
        self.nombPer = nombre
        self.edadPer = edad
        self.dniPer = DNI
    def checkNombre(self,nombre):
        if nombre.isnumeric() or len(nombre)<2:
            newName=input("Ingrese nuevamente el nombre de la persona, pero esta vez sin caracteres de tipo numerico por favor")
            self.checkNombre(newName)
        elif nombre == "":
            pass
        else:
            self.setnombre(nombre)
    def checkEdad(self,edad):
        con=False
        while con == False:
            if edad.isnumeric():
                if int(edad) >=1 and int(edad) <=99 or edad =="":
                    self.setedad(int(edad))
                    con== True
                else:
                    newEdad=input("El numero de edad ingresado es incorrecto por favor ingrese un valor entre 1 y 99 años")     
                    self.checkEdad(newEdad)
            else:
                newEdad=input("El valor de edad ingresado es incorrecto, recuerde que debe ingresar el valor de la edad en numeros, no en letras, por favor ingrese un valor entre 1 y 99 años")     
                self.checkEdad(newEdad)
    def checkDni(self,DNI):
        if DNI.isnumeric():
                if len(DNI)>5 and len(DNI)<9 or DNI=="":
                    self.setdni(int(DNI))
                else:
                    newDNI=input("El numero de DNI ingresado no es correcto, por favor ingreselo nuevamente")
                    self.checkDni(newDNI)
        else:
            newDNI=input("El numero de DNI ingresado no es correcto, solo se deben ingresar valores numericos, por favor ingreselo nuevamente")
            self.checkDni(newDNI)
        
    def getnombre(self):
        return self.nombPer
    def setnombre(self,nombre):
        self.nombPer=nombre
    def getedad(self):
        return self.edadPer
    def setedad(self,edad):
        self.edadPer=edad
    def getdni(self):
        return self.dniPer
    def setdni(self,dni):
        self.dniPer=dni
        
    def mostrar(self):
        print("los datos de la persona ingresada son: " + ""+ "Nombre:"+""+ self.nombPer +""+" Edad: "+str(self.edadPer)+""+ " DNI: " + "" + str(self.dniPer))
    def mayorEdad(self):
        if self.edadPer == "":
            pass
        elif self.edadPer > 17:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")


print("Buenos dias por favor ingrese los siguientes datos:")
nom=input("Ingrese el Nombre de la persona: ")
edad=(input("Ingrese la edad de " + nom + ".. "))
dni=(input("Ingrese el dni de " + nom + ".. "))
Human=persona(nom,edad,dni)
Human.checkEdad(edad)
Human.checkDni(dni)
Human.checkNombre(nom)      
Human.mostrar()
Human.mayorEdad()
