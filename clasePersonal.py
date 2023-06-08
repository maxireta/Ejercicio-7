class personal:
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, a, b):
        self.__cuil = cuil
        self.__ape = apellido
        self.__nom = nombre
        self.__sueldo = sueldo
        self.__ant = antiguedad
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__ape
    def getNombre(self):
        return self.__nom
    def getSueldo(self):
        return self.__sueldo
    def getAntiguedad(self):
        return self.__ant