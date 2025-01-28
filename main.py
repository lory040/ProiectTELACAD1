# Meniu Interactiv actualizat

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

        optiune = input("Alege o opțiune: ")

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
                    print("Valoare invalidă pentru rating. Introduceți un număr.")
                    continue
            elif criteriu == "an":
                try:
                    valoare = int(valoare)
                except ValueError:
                    print("Valoare invalidă pentru an. Introduceți un an valid.")
                    continue


            rezultate = biblioteca.cautare_avansata(criteriu, valoare)
            print("\nRezultate căutare:")
            if rezultate:
                for carte in rezultate:
                    print(carte)
            else:
                print("Nu au fost găsite cărți care să corespundă criteriilor.")


        elif optiune == "4":  # Raport statistic
            raport = biblioteca.raport_statistic()
            print("\nRaport Statistic:")
            print(f"Total cărți: {raport['total_carti']}")
            print(f"Cărți împrumutate: {raport['carti_imprumutate']}")
            print(f"Cărți disponibile: {raport['carti_disponibile']}")
            print("Cele mai populare 3 categorii:")
            for categorie, nr in raport['categorii_populare']:
                print(f"  {categorie}: {nr} cărți")
            print("Cei mai activi utilizatori:")
            for utilizator, nr in raport['cei_mai_activi_utilizatori']:
                print(f"  {utilizator}: {nr} împrumuturi")



        elif optiune == "5":  # Recomandări cărți
            id_utilizator = int(input("ID utilizator: "))
            recomandari = biblioteca.recomanda_carti_utilizator(id_utilizator)
            if recomandari:
                print("\nRecomandări pentru tine:")
                for carte in recomandari:
                    print(carte)
            else:
                print("Nu s-au găsit recomandări.")


        elif optiune == "6":  # Împrumut carte
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


        elif optiune == "9":  # Adăugare rating
            id_carte = int(input("ID carte: "))
            rating = float(input("Rating (1-5): "))
            biblioteca.adauga_rating_carte(id_carte, rating)


        elif optiune == "10":  # Căutare cărți cu rating > 4
            rezultate = biblioteca.cautare_rating_peste_4()
            if rezultate:
                print("\nCărți cu rating > 4:")
                for carte in rezultate:
                    print(carte)
            else:
                print("Nu s-au găsit cărți cu rating > 4.")


        elif optiune == "11":  # Sortare cărți
            criteriu_sortare = input("Criteriu (an/categorie/rating): ")
            rezultate = biblioteca.sorteaza_carti(criteriu_sortare)
            if rezultate:
                print("\nCărți sortate:")
                for carte in rezultate:
                    print(carte)
            else:
                print("Criteriu invalid sau nu s-au gasit carti pentru acest criteriu.")

        elif optiune == "12":  # Vizualizare cărți din bibliotecă
            biblioteca.vizualizare_carti()


        elif optiune == "13":  # Afisare utilizatori
            biblioteca.afiseaza_utilizatori()


        elif optiune == "14":
            print("Iesire din sistem.")
            break

        else:
            print("Opțiune invalidă. Reîncercați!")

if __name__ == "__main__":
    meniu()
