from unittest import TestCase
from Personnage import Personnage

class TestPersonnage(TestCase):

    def test_point_de_vie(self):
        personnage = Personnage()
        self.assertEqual(100, personnage.ptv)