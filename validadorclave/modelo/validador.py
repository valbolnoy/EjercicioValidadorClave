# TODO: Implementa el código del ejercicio aquí
from abc import abstractmethod, ABC
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    @staticmethod
    def _contiene_mayuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False
