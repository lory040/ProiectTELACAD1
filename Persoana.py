# 0. Clasa de Baza Persoana (abstracta)
from abc import ABC, abstractmethod

class Persoana(ABC):

    def __init__(self, id_persoana, nume):
        if not isinstance(id_persoana, int):
            raise ValueError("ID-ul persoanei trebuie sa fie un numar intreg.")
        if not isinstance(nume, str):
            raise ValueError("Numele trebuie sa fie un sir de caractere.")

        self.id_persoana = id_persoana
        self.nume = nume

    @abstractmethod
    def __str__(self):
        pass