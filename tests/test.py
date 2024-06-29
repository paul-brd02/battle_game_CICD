from unittest import TestCase
from Personnage import Personnage

class TestPersonnage(TestCase):

    def test_point_de_vie(self):
        personnage = Personnage()
        self.assertEqual(100, personnage.ptv)

    def test_tuer(self):
        personnage = Personnage()
        self.assertTrue(personnage.est_mort)