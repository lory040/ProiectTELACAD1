
class Carte:
    def __init__(self, id_carte, titlu, autor, categorie, an_publicatie):
        if not isinstance(id_carte, int):
            raise ValueError("ID-ul cartii trebuie sa fie un numar intreg.")
        if not isinstance(titlu, str) or not titlu:
            raise ValueError("Titlul cartii trebuie sa fie un sir de caractere valid.")
        if not isinstance(categorie, str) or not categorie:
            raise ValueError("Categoria trebuie sa fie un sir de caractere valid.")
        if not isinstance(an_publicatie, int) or an_publicatie < 0 or an_publicatie > 2025:
            raise ValueError("Anul de publicare trebuie sa fie un numar intre 0 si 2025.")

        self.id_carte = id_carte
        self.titlu = titlu
        self.autor = autor  #
        self.categorie = categorie
        self.an_publicatie = an_publicatie
        self.disponibila = True
        self.ratinguri = []
        self.rating_mediu = 0

    def adauga_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratinguri.append(rating)
            self.rating_mediu = sum(self.ratinguri) / len(self.ratinguri)  # Calculăm media
        else:
            print("Ratingul trebuie să fie între 1 și 5.")

    def imprumutata(self):
        self.disponibila = False  # Cartea nu mai este disponibilă pentru împrumut

    def returnata(self):
        self.disponibila = True  # Cartea devine disponibilă din nou

    @property
    def rating(self):
        return round(sum(self.ratinguri) / len(self.ratinguri), 2) if self.ratinguri else 0

    def __str__(self):
        return f"Carte: {self.id_carte}.'{self.titlu}' de {self.autor.nume} (Categorie: {self.categorie}, An: {self.an_publicatie}, Rating: {self.rating})"