# 4. Clasa Biblioteca
from functools import reduce

from Autor import Autor
from Carte import Carte
from Decoratori import logare_actiuni
from Exceptii import CarteDejaImprumutata, CarteInexistenta
from Utilizator import Utilizator


class Biblioteca:
    def __init__(self):
        self.lista_carti = []  # lista de obiecte Carte
        self.utilizatori = {}  # dictionar ID -> Utilizator
        self.id_carte_next = 1  # Counter pentru ID-uri carti
        self.id_utilizator_next = 1
        self.populate_biblioteca()

    def populate_biblioteca(self):
        # Adăugăm utilizatori
        utilizator1 = Utilizator(1, "Popa Maria")
        utilizator2 = Utilizator(2, "Pop Mihai")
        utilizator3 = Utilizator(3, "Marin Andrei")
        self.utilizatori[utilizator1.id_persoana] = utilizator1
        self.utilizatori[utilizator2.id_persoana] = utilizator2
        self.utilizatori[utilizator3.id_persoana] = utilizator3

        # Adăugăm câteva cărți
        carte1 = Carte(self.id_carte_next, "Ion", Autor(1, "Liviu Rebreanu"), "Clasic", 1920)
        carte2 = Carte(self.id_carte_next + 1, "Maitreyi", Autor(2, "Mircea Eliade"), "Romantic", 1933)
        carte3 = Carte(self.id_carte_next + 2, "Enigma Otiliei", Autor(3, "George Calinescu"), "Romantic", 1938)
        carte4 = Carte(self.id_carte_next + 3, "Padurea Spanzuratilor", Autor(4, "Liviu Rebreanu"), "Dramatic",
                           1922)
        carte5 = Carte(self.id_carte_next + 4, "Ultima noapte de dragoste", Autor(5, "Camil Petrescu"), "Clasic",
                           1930)

        self.lista_carti.extend([carte1, carte2, carte3, carte4, carte5])

       
        self.id_carte_next += 5

    @logare_actiuni
    def adauga_carte(self, carte):
        if carte not in self.lista_carti:
            carte.id_carte = self.id_carte_next
            self.lista_carti.append(carte)
            self.id_carte_next += 1
            print(f"Cartea '{carte.titlu}' a fost adaugata in biblioteca cu Id-ul {carte.id_carte}.")
        else:
            print(f"Cartea '{carte.titlu}' este deja în bibliotecă.")


    @logare_actiuni
    def adauga_utilizator(self, utilizator):
        utilizator.id_persoana = self.id_utilizator_next
        self.utilizatori[utilizator.id_persoana] = utilizator
        self.id_utilizator_next += 1
        print(f"Utilizatorul {utilizator.nume} a fost adăugat in sistem cu ID-ul {utilizator.id_persoana}.")


    def cautare_avansata(self, criteriu, valoare):
        if criteriu == "autor":
            return list(filter(lambda carte: carte.autor.nume == valoare, self.lista_carti))
        elif criteriu == "categorie":
            return list(filter(lambda carte: carte.categorie == valoare, self.lista_carti))
        elif criteriu == "an":
            return list(filter(lambda carte: carte.an_publicatie == valoare, self.lista_carti))
        elif criteriu == "rating":
            return list(filter(lambda carte: carte.rating >= valoare, self.lista_carti))
        else:
            print("Criteriu invalid.")
            return []


    def sorteaza_carti(self, criteriu):
        if criteriu == "an":
            return sorted(self.lista_carti, key=lambda carte: carte.an_publicatie)
        elif criteriu == "categorie":
            return sorted(self.lista_carti, key=lambda carte: carte.categorie)
        elif criteriu == "rating":
            return sorted(self.lista_carti, key=lambda carte: carte.rating, reverse=True)
        else:
            print("Criteriu de sortare invalid.")
            return []

    def raport_statistic(self):
        # Total carti
        total_carti = len(self.lista_carti)

        # Carti disponibile
        carti_disponibile = reduce(lambda acc, carte: acc + (1 if carte.disponibila else 0), self.lista_carti, 0)

        # Carti imprumutate 
        carti_imprumutate = total_carti - carti_disponibile

        # Cele mai populare 3 categorii
        categorii_populare = reduce(
            lambda acc, carte: acc.update({carte.categorie: acc.get(carte.categorie, 0) + 1}) or acc, self.lista_carti,
            {})
        cele_mai_populare = sorted(categorii_populare.items(), key=lambda x: x[1], reverse=True)[:3]

        # Cei mai activi utilizatori 
        activitate_utilizatori = {utilizator: utilizator.contor_imprumuturi for utilizator in self.utilizatori.values()}
        cei_mai_activi = sorted(activitate_utilizatori.items(), key=lambda x: x[1], reverse=True)[:3]

        # Returneaza toate statisticile
        return {
            "total_carti": total_carti,
            "carti_imprumutate": carti_imprumutate,
            "carti_disponibile": carti_disponibile,
            "categorii_populare": cele_mai_populare,
            "cei_mai_activi_utilizatori": cei_mai_activi
        }


    def recomanda_carti(self, utilizator):
        recomandari = []

        # 1. Recomanda carti din aceeasi categorie
        for carte in utilizator.carti_imprumutate:
            for c in self.lista_carti:
                if c.categorie == carte.categorie and c not in utilizator.carti_imprumutate:
                    recomandari.append(c)

        # 2. Recomanda carti populare (cele mai imprumutate)
        carti_populare = sorted(self.lista_carti, key=lambda x: len(x.carti_imprumutate), reverse=True)
        for c in carti_populare[:3]:
            if c not in utilizator.carti_imprumutate:
                recomandari.append(c)

       
        if not recomandari:
            print("Nu există recomandări pe baza cărților împrumutate.")
        else:
            print("Recomandări pentru tine:")
            for c in recomandari:
                print(f"- {c.titlu} de {c.autor.nume}")


    def returneaza_carte(self, id_utilizator, id_carte):
        utilizator = self.utilizatori.get(id_utilizator)
        carte = next((c for c in self.lista_carti if c.id_carte == id_carte), None)

        if utilizator and carte:
            utilizator.returneaza_carte(carte)
            print(f"Cartea '{carte.titlu}' a fost returnată de către utilizatorul {utilizator.nume}.")
        else:
            print("Utilizator sau carte inexistentă.")


    def recomanda_carti_utilizator(self, id_utilizator):
        utilizator = self.utilizatori.get(id_utilizator)
        if utilizator:
            categorii_preferate = [carte.categorie for carte in utilizator.carti_imprumutate]
            recomandari = filter(lambda carte: carte.categorie in categorii_preferate and carte.disponibila,
                                 self.lista_carti)
            return list(recomandari)
        else:
            print("Utilizator inexistent.")
            return []


    def imprumuta_carte(self, id_utilizator, id_carte):
        utilizator = self.utilizatori.get(id_utilizator)
        carte = next((c for c in self.lista_carti if c.id_carte == id_carte), None)

        if utilizator and carte:
            try:
                utilizator.imprumuta_carte(carte)
            except CarteDejaImprumutata as e:
                print(e)  
            except CarteInexistenta as e:
                print(e)  
        else:
            print("Utilizator sau carte inexistentă.")



    def afiseaza_statistici_utilizator(self, id_utilizator):
        utilizator = self.utilizatori.get(id_utilizator)
        if utilizator:
            print(utilizator.statistici_personale())
        else:
            print("Utilizator inexistent.")


    def adauga_rating_carte(self, id_carte, rating):
        carte = next((c for c in self.lista_carti if c.id_carte == id_carte), None)
        if carte:
            carte.adauga_rating(rating)
            print(f"Ratingul {rating} a fost adăugat la cartea '{carte.titlu}'.")
        else:
            print("Cartea nu a fost găsită.")


    def cautare_rating_peste_4(self):
        return list(filter(lambda carte: carte.rating > 4, self.lista_carti))


    def vizualizare_carti(self):
        if self.lista_carti:
            print("\nCărți din bibliotecă:")
            for carte in self.lista_carti:
                print(carte)
        else:
            print("Nu sunt cărți în bibliotecă.")


    def afiseaza_utilizatori(self):
        if self.utilizatori:
            print("\nUtilizatori înregistrați:")
            for utilizator in self.utilizatori.values():
                print(f"ID: {utilizator.id_persoana}, Nume: {utilizator.nume}")
        else:
            print("Nu există utilizatori înregistrați.")


    def __str__(self):
        return f"Biblioteca contine {len(self.lista_carti)} carti si {len(self.utilizatori)} utilizatori."
