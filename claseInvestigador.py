from clasePersonal import personal

class investigador(personal):
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, area, tipo):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__area = area
        self.__tipo = tipo
    def __str__(self):
        return f"Investigador: {super().getApellido()} {super().getNombre()}, Area: {self.__area}"
    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo
    def getApe(self):
        return super().getApellido()
    def getSueldo(self):
        return super().getSueldo()
    def dic(self):
        return {
            "cuil": super().getCuil(),
            "apellido": super().getApellido(),
            "nombre": super().getNombre(),
            "sueldo": super().getSueldo(),
            "antiguedad": super().getAntiguedad(),
            "area": self.__area,
            "tipo": self.__tipo
        }