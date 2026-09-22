#Import la classe Habitant d
from habitant import Habitant

class Village:
    """
    Classe représentant un village.
    """
    def __init__(self, nom):
        self.__nom = nom
        self.__habitants = []


    def get_habitants(self):
        """
        renvoie la liste des habitants du village
        """
        return self.__habitants

    def ajouter_habitant_composition(self, nom, age, adresse, animaux = None):
        """
        Ajoute un nouvel habitant
        """
        self.__habitants.append(Habitant(nom, age, adresse, animaux))
    
    def ajouter_habitant_agregation(self, habitant):
        """
        Ajoute un habitant existant
        """
        if isinstance(habitant, Habitant):
            self.__habitants.append(habitant)
        else :
            raise ValueError("L'habitant doit être une instance de la classe Habitant.")
    
    def afficher_habitants(self):
        """
        Affiche chaque habitant du village
        """
        for habitant in self.__habitants:
            print(f"{habitant.get_nom()} habite à {habitant.get_adresse()}")

"""
Jeu de test pour la classe village et ses méthodes
"""
pytown = Village("PyTown")

pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})

pytown.ajouter_habitant_agregation(elise)

autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

"""
par composition on créer habitant dans la fonction, donc si le constructeur est supprimé, habitant aussi car il n'existe pas indépendament de la structure

par agrégation, habitant est en paramètre, il existe déjà indépendamment de la structure. Donc si c'est supprimé, habitant existe toujours



"""