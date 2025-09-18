def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    #TODO : Creer 3 listes

    #TODO : Pour 3 ordinateur
        #TODO : Demander temp, pousssiere, humidit
        #TODO : Mettres les 3 valeurs dans leurs listes

    temp = int(input("Entrez la temperature"))
    poussiere = input("Entrez le niveau de poussiere: ")
    humidite = float(input("Entrez l'humidite: "))


    #TODO : Pour les 3 ordi
        #TODO : utiliser la fonction et afficher le resultat
    print(environnement_optimal(temp, poussiere, humidite))
