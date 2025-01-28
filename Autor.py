# 2. Clasa Autor
class Autor:
    def __init__(self, id_autor, nume):

        if not isinstance(id_autor, int):
            raise ValueError("ID-ul autorului trebuie sa fie un numar intreg.")
        if not isinstance(nume, str):
            raise ValueError("Numele autorului trebuie sa fie un sir de caractere.")

        self.id_autor = id_autor
        self.nume = nume
        self.carti_scrise = []  # listă de obiecte Carte

    def adauga_carte(self, carte):
        if carte in self.carti_scrise:
            print(f"Cartea '{carte.titlu}' este deja adăugată la autorul {self.nume}.")
        else:
            self.carti_scrise.append(carte)
            print(f"Cartea '{carte.titlu}' a fost adăugată la autorul {self.nume}.")

    def __str__(self):
        return f"Autor: {self.nume} (ID: {self.id_autor})"
