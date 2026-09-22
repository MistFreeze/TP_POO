"""
Tests unitaires pour les classes Habitant, Adulte et Enfant.
"""

import unittest
from habitant import Habitant, Adulte, Enfant

class TestHabitant(unittest.TestCase):
    """Tests de la classe de base Habitant."""

    def test_attributs_initiaux(self):
        self.assertEqual(self.h.get_nom(), "Aldric")
        self.assertEqual(self.h.age, 25)
        self.assertEqual(self.h.get_adresse(), "Rue A")

    def test_nom_prive(self):
        # Vérifie l'encapsulation via le name mangling
        self.assertEqual(self.h._Habitant__nom, "Aldric")

    def test_get_set_nom(self):
        self.h.set_nom("Bertrand")
        self.assertEqual(self.h.get_nom(), "Bertrand")

    def test_get_set_adresse(self):
        self.h.set_adresse("Rue B")
        self.assertEqual(self.h.get_adresse(), "Rue B")

    def test_habitant_est_abstraite(self):
        # Habitant hérite d'ABC et déclare une méthode abstraite :
        # elle ne doit pas pouvoir être instanciée directement.
        with self.assertRaises(TypeError):
            Habitant("X", 30, "Rue Z")


class TestAdulte(unittest.TestCase):
    """Tests de la classe dérivée Adulte."""

    def test_heritage(self):
        self.assertIsInstance(self.adulte, Habitant)

    def test_attributs_herites(self):
        self.assertEqual(self.adulte.get_nom(), "Dupont")
        self.assertEqual(self.adulte.age, 35)
        self.assertEqual(self.adulte.get_adresse(), "Rue A")


    def test_age_limite_18_valide(self):
        # 18 ans doit être accepté (borne incluse)
        a = Adulte("Limite", 18, "Rue D")
        self.assertEqual(a.age, 18)

    def test_calcul_avant_retraite_actif(self):
        self.assertEqual(self.adulte.calcul_nombre_annee_avant_retraite(), 27)

    def test_calcul_avant_retraite_deja_retraite(self):
        retraite = Adulte("Retraité", 65, "Rue E")
        self.assertEqual(
            retraite.calcul_nombre_annee_avant_retraite(), "Deja a la retraite"
        )


class TestEnfant(unittest.TestCase):
    """Tests de la classe dérivée Enfant."""

    def setUp(self):
        self.enfant = Enfant("Martin", 12, "Rue B")

    def test_heritage(self):
        self.assertIsInstance(self.enfant, Habitant)

    def test_attributs_herites(self):
        self.assertEqual(self.enfant.get_nom(), "Martin")
        self.assertEqual(self.enfant.age, 12)

    def test_age_trop_grand_leve_erreur(self):
        with self.assertRaises(ValueError):
            Enfant("Trop Vieux", 18, "Rue C")  # 18 doit être refusé pour un enfant

    def test_calcul_avant_retraite_message_erreur(self):
        resultat = self.enfant.calcul_nombre_annee_avant_retraite()
        self.assertIn("enfant", resultat.lower())


if __name__ == "__main__":
    unittest.main()