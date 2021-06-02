for i in range(0,5):

    class Resgistrar:
        def __init__(self, identificacion, nombre , salario) :
            
            
            self.identificacion = input('digite la identificacion : ')
            identificacion=identificacion
            self.nombre = input('  nombre completos : ' )
            nombre=nombre
            self.salario =  int(input('ingrese el salirio : '))
            salario=salario


        def __str__(self):
            return "identificacion: " + self.identificacion + ", nombre: "+ str(self.nombre) + ", salario: " + str(self.salario)


    class Insertar(Resgistrar):
        def __init__(self, identificacion, nombre, salario, comision, bonificacion) :
            super().__init__(identificacion, nombre, salario) 
            total=0 
            self.comision =comision  
            self.bonificacion =  bonificacion
            if salario > "900000":
                total= bonificacion+comision
                print(f'tienen derecho a bonificacion {salario}') 
            else:
                total=salario
                print(f"No tiene derecho bonificacion {salario}")

            print(salario) 
                 
            print(f"esta es la total sin bonificacion {total}")         

        def __str__(self):
            return super().__str__() + ", comision: " + str(self.comision) + ", bonificacion: " + str(self.bonificacion)
        

    resgistrar = Resgistrar
      
    print(resgistrar)

     
    insertar = Insertar("","", "","12000","10000") 

    print(insertar)

resgistrar = Resgistrar
 
print(resgistrar)
  
insertar = Insertar("","", "","12000","10000") 
print(insertar)

print(f"lista de  {i}")


        
