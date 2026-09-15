import unittest

#création d'une classe de test pour chaque exo

class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""

    def test_recalibrer_capteur_existant(self):
        """Cas normal : le capteur existe dans la liste des relevés."""
        releves = [
            ("laser_avant", 2.35, "m"),
            ("laser_arriere", 1.10, "m"),
            ("gyroscope", 87.5, "deg")
        ]
        nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
        
        #assertequal vérifie que les valeurs sont égales, sinon le test échoue
        self.assertEqual(nouveaux_releves[0], ("laser_avant", 2.40, "m"))
        self.assertEqual(nouveaux_releves[1], ("laser_arriere", 1.10, "m"))
        self.assertEqual(nouveaux_releves[2], ("gyroscope", 87.5, "deg"))

       
    def test_recalibrer_capteur_absent(self):   
        """Cas limite : le capteur demandé n'existe pas."""
        releves = [
            ("laser_avant", 2.35, "m"),
            ("laser_arriere", 1.10, "m"),
            ("gyroscope", 87.5, "deg")
        ]
        nouveaux_releves = recalibrer(releves, "capteur_inexistant", 3.00)
        self.assertEqual(nouveaux_releves, releves)  # Aucun changement attendu


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Exécute les tests avec un niveau de détail élevé
    
