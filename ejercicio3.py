class Vehiculos():
    def __init__(self, _matricula, _medio, _cap_pasajeros, _vel_max):
        self.matricula = _matricula
        self.medio = _medio
        self.cap_pasajeros = _cap_pasajeros
        self.vel_max = _vel_max

class Maritimos(Vehiculos):
    def __init__(self, _tipo_propulsion):
        self.tipo_propulsion = _tipo_propulsion

class Aereos(Vehiculos):
    def __init__(self):

class Terrestres(Vehiculos):
    def __init__(self, _no_ruedas, _datos_motor, _no_puertas):
        self.no_ruedas = _no_ruedas
        self.datos_motor = _datos_motor
        self.no_puertas = _no_puertas


