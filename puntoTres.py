class Resgistrar:
    def __init__(self, placa, entrada, salida, celda ) :
        self.placa = input(' numero de placa : ')
        placa=placa
        self.entrada = input('fecha de entrada : ' )
        entrada=entrada
        self.salida =  input(' fecha de salida : ')
        salida=salida
        self.celda =  input(' celda de parqueo : ')
        celda=celda


    def __str__(self):
        return "placa: " + self.placa + ", entrada: "+ str(self.entrada) + ", salida: " + str(self.salida) + ", parqueo: " + str(self.celda)

class Insertar(Resgistrar):
    def __init__(self, placa, entrada, salida, celda, tiempo, parqueado) :
        super().__init__(placa, entrada, salida, celda) 
        total=0 
        self.tiempo =tiempo  
        self.parqueado =  parqueado
        if salida > entrada:
            total= tiempo+parqueado
            print(f'este es valor a pagar {total}') 
        else:
             total=celda
             print(f"parquedero  {celda}")

        print(celda) 
        print(f"esta es la total a pagar {total}")         

    def __str__(self):
        return super().__str__() + ", tiempo: " + str(self.tiempo) + ", parqueado: " + str(self.parqueado)
resgistrar = Resgistrar
print(resgistrar)
insertar = Insertar("","","","",24,18000) 
print(insertar)