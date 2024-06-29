class Personnage():
    def __init__(self) -> None:
        self.ptv = 100
        self.est_mort = False

    def tuer(self):
        self.est_mort = True
        self.ptv = 0
    
    def attaque(self, personnage:'Personnage'):
        personnage.ptv -= 20