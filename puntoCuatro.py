for i in range(2):
    class Matricula:
        def __init__(self, matricula, nombre, dirrecion, telefono, curso):
            self.__matricula = input("numero de matricula : ")
            matricula=matricula
            self.__nombre = input("nombre : ")
            nombre=nombre
            self.__dirrecion = input("dirrecion : ")
            dirrecion=dirrecion
            self.__telefono = input("telefono : ")
            telefono = telefono 
            self.__curso =  input("curso : ")
            curso=curso

        def get_matricula(self):
                return self.__matricula           
        def set_matricula(self, matricula):
            self.__matricula = matricula


        def get_nombre(self):
                return self.__nombre           
        def set_nombre(self, nombre):
            self.__nombre = nombre

        def get_dirrecion(self):
                return self.__dirrecion           
        def set_dirrecion(self, dirrecion):
            self.__dirrecion = dirrecion

        def get_telefono(self):
                return self.__telefono           
        def set_telefono(self, telefono):
            self.__telefono = telefono

        def get_curso(self):
                return self.__curso           
        def set_curso(self, curso):
            self.__curso = curso
print()
p1 = Matricula("","","","","")
print()
print('Datos del alumno ')
print()
print("Numero de matricula : "+p1.get_matricula())
print("Nombre del alumno :  "+p1.get_nombre())
print("Dirrecion del alumno :  " + p1.get_dirrecion())
print("Telefono del alumno :  " + p1.get_telefono())
print("Esta en el curso :  " + p1.get_curso())