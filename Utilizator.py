# 1. Clasa Utilizator (derivata din Persoana)
from Exceptii import CarteDejaImprumutata
from Persoana import Persoana


class Utilizator(Persoana):
    def __init__(self, id_persoana, nume):
        super().__init__(id_persoana, nume)
        self.carti_imprumutate = []  # lista de obiecte Carte
        self.istoric_imprumuturi = set()  # set de titluri
        self.contor_imprumuturi = 0  # adăugăm un contor pentru împrumuturi


    def imprumuta_carte(self, carte):
        if carte.disponibila:  # Verifică dacă cartea este disponibilă pentru împrumut
            if carte.titlu not in self.istoric_imprumuturi:
                self.carti_imprumutate.append(carte)
                self.istoric_imprumuturi.add(carte.titlu)  # adăugăm titlul în istoric
                self.contor_imprumuturi += 1  # incrementăm contorul de împrumuturi
                carte.imprumutata()  # Marca cartea ca împrumutată
                print(f"Cartea '{carte.titlu}' a fost împrumutată de {self.nume}.")
            else:
                raise CarteDejaImprumutata(f"Cartea '{carte.titlu}' a fost deja împrumutată.")
        else:
            print(f"Cartea '{carte.titlu}' nu este disponibilă pentru împrumut.")


    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            self.carti_imprumutate.remove(carte)
            carte.disponibila = True
            print(f"{self.nume} a returnat cartea '{carte.titlu}'.")
        else:
            print(f"Cartea '{carte.titlu}' nu a fost imprumutată de {self.nume}.")

    def statistici_personale(self):

        return f"{self.nume} a imprumutat {len(self.istoric_imprumuturi)} carti in total."

    def __str__(self):
        return f"Utilizator: {self.nume} (ID: {self.id_persoana})"
