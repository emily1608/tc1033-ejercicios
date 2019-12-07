class Motor():
    def __init__(self, _combustible, _fabricante, _potencia):
        self.combustible = _combustible
        self.fabricante = _fabricante
        self.potencia = _potencia
        
class Vehiculos():
    def __init__(self, _matricula, _medio, _cap_pasajeros, _vel_max, _tipo):
        self.matricula = _matricula
        self.medio = _medio
        self.cap_pasajeros = _cap_pasajeros
        self.vel_max = _vel_max
        self.tipo = _tipo

class Maritimos(Vehiculos):
    def __init__(self, _tipo_propulsion):
        self.tipo_propulsion = _tipo_propulsion

class Aereos(Vehiculos):
    def __init__(self, _tipo_propulsion):
        self.tipo_propulsion = _tipo_propulsion

class Terrestres(Vehiculos):
    def __init__(self, _no_ruedas, _datos_motor, _no_puertas):
        self.no_ruedas = _no_ruedas
        self.datos_motor = _datos_motor
        self.no_puertas = _no_puertas

class Ruedas():
    def __init__(self, _tamaño_in, _presion_ideal, _fabricante):
        self.tamaño_in = _tamaño_in
        self.presion_ideal = _presion_ideal
        self.fabricante = _fabricante

class Propulsión():
    def __init__(self, _vela, _motor, _remo):
        self.vela = _vela
        self.motor = _motor
        self.remo = _remo


