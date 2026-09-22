"""
Création d'une classa Habitant et de 2 méthodes.

"""


class Habitant(object):
    """
    Classe représentant un habitant.
    """
    def __init__(self, nom, age, adresse, animaux = None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}


    def affichage_adresse(self):
        """
        Affiche l'adresse de l'habitant.
        """
        print(f"{self.nom} habite à {self.adresse}")

    def compte_animaux(self, animal):
        """
        Compte le nombre d'animaux de l'habitant.
        """
        return self.animaux.get(animal, 0)

#Création d'un habitant
h1  = Habitant("Aldric", 25, "Rue A", {"vaches":3})

"""
Test de la classe Habitant et de ses méthodes.
"""
assert h1.nom == "Aldric"
assert h1.compte_animaux("vaches") == 3
assert h1.compte_animaux("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"
