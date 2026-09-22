"""
Création d'une classa Habitant et de 2 méthodes.

"""
from multipledispatch import dispatch
from abc import ABC


class Habitant(ABC): #Habitant hérite d'ABC
    """
    Classe représentant un habitant.
    tous les attributs sont privés.
    """
    def __init__(self, nom, age, adresse, animaux = None):
        self.__nom = nom
        self.age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    def affichage_adresse(self):
        """
        Affiche l'adresse de l'habitant.
        """
        print(f"{self.__nom} habite à {self.__adresse}")

    def compte_animaux(self, animal):
        """
        Compte le nombre d'animaux de l'habitant.
        """
        return self.__animaux.get(animal, 0)

    """
    Ajout des accesseurs et mutateurs pour tous les attributs.
    """
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 150:
            raise ValueError("L'âge doit être compris entre 0 et 150 ans.")
        self.__age = age

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, adresse):
        # Vérification que l'adresse est une chaîne de caractères
        if isinstance(adresse, str):
            self.__adresse = adresse
        else:
            raise ValueError("L'adresse doit être une chaîne de caractères.")
            
    def get_animaux(self):
        return self.__animaux
    
    def set_animaux(self, animaux):
        # Vérification que les animaux sont un dictionnaire
        if isinstance(animaux, dict):
            self.__animaux = animaux
        else:
            raise ValueError("Les animaux doivent être un dictionnaire.")


    @dispatch(object, str)
    def set_info(habitant, nom):
        """Surchage pour string"""
        habitant.set_nom = nom

    @dispatch(object, str, int)
    def set_info(habitant, nom, age):
        """ Surchage pour un string + int """
        habitant.set_nom = nom
        habitant.age = age
        
        @abstractmethod
        #toute classe qui hérité de cnaar doit l'implémenter elle même sinon considéré comme abstraite
        def calcul_nombre_annee_avant_retraite(self):
            pass
                    
"""
les méthodes/classe abstraite, sont utilisées pour ne pas être des classes principales, mais pour être utiliser. Elles servent de bases.

"""


class Adulte(Habitant): #Classe adulte hérite de la classe Habitant
    def __init__(self, nom, age, adresse):
        if age < 18 :
            raise ValueError("Un adulte doit avoir 18 ou plus")
        super().__init__(nom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà retraité"
        else :
            return age_retraite - self.age

class Enfant(Habitant):
    def __init__(self, nom, age, adresse):
        if age >=18:
            raise ValueError("un enfant à moins de 18ans")
        super().__init__(nom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur : Un enfant ne peut pas calculer sa retraite"



def __str__(self):
    return f"{self.nom()}, {self.age()} ans, habite à {self.adresse()}"

def affichage(h: Habitant): #dis que h est de type habitant
    """Affichage d'un habitant"""
    print(str(h))





#Création d'un habitant
h1  = Habitant("Aldric", 25, "Rue A", {"vaches":3})
h1.age = 26
assert h1.age == 26

try:
    h1.age = -5
    assert False, "Une ValueError aurait dû être levée"
except ValueError:
    pass

"""
Test de la classe Habitant et de ses méthodes.
"""
assert h1._Habitant__nom == "Aldric"
assert h1.compte_animaux("vaches") == 3
assert h1.compte_animaux("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"


# Adulte : leve une ValueError si age < 18
# calcul_nombre_annee_avant_retraite() renvoie :
# - "Deja a la retraite" si age >= 62
# - 62 - age sinon
# Enfant : leve une ValueError si age >= 18
# calcul_nombre_annee_avant_retraite() renvoie toujours :
# - "Erreur: un enfant ne peut pas calculer sa retraite"


adulte = Adulte("Dupont", 35, "Rue A")
enfant = Enfant("Martin", 12, "Rue B")

assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

try:
    Enfant("Oups", 25, "Rue C")
    assert False, "une ValueError aurait dû être levée"
except ValueError :
    pass

affichage(adulte)
affichage(enfant)
# Chaque habitant s’affiche correctement, quel que soit son type reel
