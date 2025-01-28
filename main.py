# Meniu Interactiv

from Utilizator import Utilizator
from Autor import Autor
from Carte import Carte
from Biblioteca import Biblioteca

def meniu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistem de Management al Bibliotecii ---")
        print("1. Adauga carte")
        print("2. Adauga utilizator")
        print("3. Cauta carti")
        print("4. Vizualizeaza raport statistic")
        print("5. Recomanda carti")
        print("6. Imprumuta carte")
        print("7. Returneaza carte")
        print("8. Statistici personale utilizator")
        print("9. Adauga rating")
        print("10. Afisare cele mai bine cotate carti")
        print("11. Sortare carti")
        print("12. Vizualizeaza carti din biblioteca")
        print("13. Vizualizeaza utilizatori din biblioteca")
        print("14. Iesire")

        optiune = input("Alege o optiune: ")

        if optiune == "1":
            titlu = input("Titlu carte: ")
            nume_autor = input("Autor: ")
            categorie = input("Categorie: ")
            an_publicatie = int(input("An publicatie: "))
            autor = Autor(len(biblioteca.lista_carti) + 1, nume_autor)
            carte = Carte(len(biblioteca.lista_carti) + 1, titlu, autor, categorie, an_publicatie)
            biblioteca.adauga_carte(carte)  # Nu mai adăuga cartea manual în lista_carti
            autor.adauga_carte(carte)  # Adaugă cartea și autorului



        elif optiune == "2":
            nume = input("Nume utilizator: ")
            utilizator = Utilizator(len(biblioteca.utilizatori) + 1, nume)
            biblioteca.adauga_utilizator(utilizator)


        elif optiune == "3":
            criteriu = input("Criteriu (autor/categorie/an/rating): ").lower()
            valoare = input("Valoare criteriu: ")
            if criteriu == "rating":
                try:
                    valoare = float(valoare)
                except ValueError:
                    print("Valoare invalida pentru rating. Introduceti un numar.")
                    continue
            elif criteriu == "an":
                try:
                    valoare = int(valoare)
                except ValueError:
                    print("Valoare invalida pentru an. Introduceti un an valid.")
                    continue


            rezultate = biblioteca.cautare_avansata(criteriu, valoare)
            print("\nRezultate căutare:")
            if rezultate:
                for carte in rezultate:
                    print(carte)
            else:
                print("Nu au fost gasite carti care să corespunda criteriilor.")


        elif optiune == "4":  # Raport statistic
            raport = biblioteca.raport_statistic()
            print("\nRaport Statistic:")
            print(f"Total carti: {raport['total_carti']}")
            print(f"Carti imprumutate: {raport['carti_imprumutate']}")
            print(f"Carti disponibile: {raport['carti_disponibile']}")
            print("Cele mai populare 3 categorii:")
            for categorie, nr in raport['categorii_populare']:
                print(f"  {categorie}: {nr} carti")
            print("Cei mai activi utilizatori:")
            for utilizator, nr in raport['cei_mai_activi_utilizatori']:
                print(f"  {utilizator}: {nr} imprumuturi")



        elif optiune == "5":  # Recomandari carti
            id_utilizator = int(input("ID utilizator: "))
            recomandari = biblioteca.recomanda_carti_utilizator(id_utilizator)
            if recomandari:
                print("\nRecomandari pentru tine:")
                for carte in recomandari:
                    print(carte)
            else:
                print("Nu s-au găsit recomandari.")


        elif optiune == "6":  # Imprumut carte
            id_utilizator = int(input("ID utilizator: "))
            id_carte = int(input("ID carte: "))
            biblioteca.imprumuta_carte(id_utilizator, id_carte)


        elif optiune == "7":  # Returnare carte
            id_utilizator = int(input("ID utilizator: "))
            id_carte = int(input("ID carte: "))
            biblioteca.returneaza_carte(id_utilizator, id_carte)


        elif optiune == "8":  # Statistici utilizator
            id_utilizator = int(input("ID utilizator: "))
            biblioteca.afiseaza_statistici_utilizator(id_utilizator)


        elif optiune == "9":  # Adaugare rating
            id_carte = int(input("ID carte: "))
            rating = float(input("Rating (1-5): "))
            biblioteca.adauga_rating_carte(id_carte, rating)


        elif optiune == "10":  # Cautare carti cu rating > 4
            rezultate = biblioteca.cautare_rating_peste_4()
            if rezultate:
                print("\nCarti cu rating > 4:")
                for carte in rezultate:
                    print(carte)
            else:
                print("Nu s-au gasit carti cu rating > 4.")


        elif optiune == "11":  # Sortare carti
            criteriu_sortare = input("Criteriu (an/categorie/rating): ")
            rezultate = biblioteca.sorteaza_carti(criteriu_sortare)
            if rezultate:
                print("\nCarti sortate:")
                for carte in rezultate:
                    print(carte)
            else:
                print("Criteriu invalid sau nu s-au gasit carti pentru acest criteriu.")

        elif optiune == "12":  # Vizualizare carti din biblioteca
            biblioteca.vizualizare_carti()


        elif optiune == "13":  # Afisare utilizatori
            biblioteca.afiseaza_utilizatori()


        elif optiune == "14":
            print("Iesire din sistem.")
            break

        else:
            print("Optiune invalida. Reincercati!")

if __name__ == "__main__":
    meniu()
