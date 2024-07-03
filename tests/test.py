from unittest import TestCase
from Personnage import Personnage

class TestPersonnage(TestCase):

    def test_point_de_vie(self):
        personnage = Personnage()
        self.assertEqual(100, personnage.get_point_de_vie())

    def test_tuer(self):
        personnage = Personnage()
        personnage.tuer()
        self.assertTrue(personnage.get_est_mort())
        self.assertEqual(0, personnage.get_point_de_vie())
    
    def test_vivant(self):
        personnage = Personnage()
        self.assertFalse(personnage.get_est_mort())
    
    def test_attaque(self):
        personnage1 = Personnage()
        personnage2 = Personnage()
        personnage2_point_de_vie = personnage2.get_point_de_vie()
        personnage1.attaque(personnage2)
        self.assertNotEqual(personnage2_point_de_vie, personnage2.get_point_de_vie())
    
    def test_point_attaque(self):
        personnage = Personnage()
        self.assertEqual(50, personnage.get_point_attaque())

    def test_reduire_point_de_vie(self):
        personnage = Personnage()
        personnage.reduire_point_de_vie(50)
        self.assertEqual(50, personnage.get_point_de_vie())

    def test_initiliasation_point_de_vie(self):
        personnage = Personnage()
        personnage.set_point_de_vie(70)
        self.assertEqual(70, personnage.get_point_de_vie())
