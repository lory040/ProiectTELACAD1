class CarteDejaImprumutata(Exception):
    def __init__(self, mesaj="Cartea este deja imprumutata."):
        super().__init__(mesaj)

class CarteInexistenta(Exception):
    def __init__(self, mesaj="Cartea nu exista in sistem."):
        super().__init__(mesaj)
