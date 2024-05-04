from carte import Carte

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []  # Liste pour stocker les cartes du joueur

    def ajouter_carte(self, valeur, couleur):
        carte = Carte(valeur, couleur)
        self.main.append(carte)

    def afficher_main(self):
        for i, carte in enumerate(self.main, start=1):
            print(f"{i}. {carte}")
        print(f"{i}. {carte}")

    def jouer_carte(self, carte_precedente):
        cartes_couleur_demandee = [carte for carte in self.main if carte.couleur == carte_precedente.couleur]

        if cartes_couleur_demandee:
            # Si le joueur a des cartes de la même couleur que la carte précédente, il doit les jouer
            carte_a_jouer = min(cartes_couleur_demandee, key=lambda carte: carte.points())
        else:
            # Si le joueur n'a pas de cartes de la même couleur que la carte précédente, il peut jouer n'importe quelle carte de sa main
            carte_a_jouer = min(self.main, key=lambda carte: carte.points())

        self.main.remove(carte_a_jouer)  # Retire la carte jouée de la main du joueur
        return carte_a_jouer  # Renvoie la carte jouée

    def ramasser_pli(self, pli):
        self.main.extend(pli)  # Ajoute les cartes du pli à la main du joueur

    def calculer_points(self):
        return sum(carte.points() for carte in self.main)  # Calcule le total des points de la main du joueur
