import pytest # importer le module pytest pour faire nos tests unitaires
from ExDebug1 import environnement_optimal # importer la fonction de notre autre fichier


# test unitaire pour la fonction environment_optimal()
def test_environnement_optimal():
    #Arrange : preparer des variables d'entrees et le resultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous controle!"

    #Act: appeler la fonction a tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: verifier le resultat
    assert resultat_attendu == resultat_obtenu

# test unitaire pour la fonction environment_optimal()
def test_environnement_optimal_2():
    #Arrange : preparer des variables d'entrees et le resultat attendu
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction a tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: verifier le resultat
    assert resultat_attendu == resultat_obtenu

# test unitaire pour la fonction environment_optimal()
def test_environnement_optimal_3():
        # Arrange : preparer des variables d'entrees et le resultat attendu
        temperature = 25
        poussiere = "faible"
        humidite = 20
        resultat_attendu = "Environnement non optimal"

        # Act: appeler la fonction a tester
        resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

        # Assert: verifier le resultat
        assert resultat_attendu == resultat_obtenu

 # test unitaire pour la fonction environment_optimal()
def test_environnement_optimal_4():
            # Arrange : preparer des variables d'entrees et le resultat attendu
            temperature = 30
            poussiere = "faible"
            humidite = 25
            resultat_attendu = "Environnement non optimal"

            # Act: appeler la fonction a tester
            resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

            # Assert: verifier le resultat
            assert resultat_attendu == resultat_obtenu