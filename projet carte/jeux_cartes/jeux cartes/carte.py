class Carte:
    """
    La classe Carte représente une carte de jeu.
    
    Attributes:
        couleurs_valides (tuple): Les couleurs valides d'une carte.
        valeurs_valides (tuple): Les valeurs valides d'une carte.
        valeur (int or str): La valeur de la carte.
        couleur (str): La couleur de la carte.
    """
    couleurs_valides = ("TREFLE", "CARREAU", "COEUR", "PIQUE")
    valeurs_valides = tuple(list(range(1, 11)) + ["VALET", "DAME", "ROI"])

    def __init__(self, valeur, couleur):
        """
        Initialise une instance de la classe Carte.
        
        Args:
            valeur (int or str): La valeur de la carte.
            couleur (str): La couleur de la carte.
        """
        self.valeur = valeur
        self.couleur = couleur

    def points(self):
        """
        Retourne les points associés à la carte.
    
        """
        if self.valeur == "DAME":
            return 10
        elif self.valeur == "ROI" and self.couleur == "COEUR":
            return 40
        elif self.couleur == "COEUR":
            return 1
        else:
            return 0

    def __repr__(self):
        """
        Retourne une représentation de la carte sous forme de chaîne de caractères.
        
        """
        return f"<Carte {self.valeur} de {self.couleur}>"

