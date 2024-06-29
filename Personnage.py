class Personnage():
    def __init__(self) -> None:
        self.__point_de_vie = 100
        self.__point_attaque = 50
        self.__est_mort = False

    def get_point_de_vie(self):
        return self.__point_de_vie

    def get_point_attaque(self):
        return self.__point_attaque

    def get_est_mort(self):
        return self.__est_mort

    def set_point_de_vie(self, value: int):
        self.__point_de_vie = value

    def set_point_attaque(self, value: int):
        self.__point_attaque = value

    def set_est_mort(self):
        self.__est_mort = True

    def tuer(self):
        self.set_point_de_vie(0)
        self.set_est_mort()
    
    def reduire_point_de_vie(self, value: int):
        self.set_point_de_vie(self.__point_de_vie - value)
    
    def attaque(self, personnage:'Personnage'):
        attaque = self.get_point_attaque()
        if attaque > personnage.get_point_de_vie():
            personnage.set_point_de_vie(0)
        else:
            personnage.reduire_point_de_vie(attaque)
    

    