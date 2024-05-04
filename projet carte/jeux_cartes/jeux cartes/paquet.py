from carte import Carte  # Importe la classe Carte depuis le module carte
import random  # Importe le module random pour mélanger les cartes

class Paquet:
    def __init__(self):
        self.cartes = []  # Initialise une liste vide pour stocker les cartes
        for valeur in Carte.valeurs_valides:  # Parcourt les valeurs valides des cartes
            for couleur in Carte.couleurs_valides:  # Parcourt les couleurs valides des cartes
                c = Carte(valeur, couleur)  # Crée une nouvelle instance de la classe Carte avec la valeur et la couleur actuelles
                self.cartes.append(c)  # Ajoute la carte à la liste des cartes du paquet

    def melanger(self):
        random.shuffle(self.cartes)  # Mélange les cartes dans le paquet en utilisant la fonction shuffle du module random

    def piocher(self):
        return self.cartes.pop()  # Retire et retourne la dernière carte du paquet

    def distribuer(self, nb_joueurs, nb_cartes):
        distributions = [[] for _ in range(nb_joueurs)]  # Crée une liste de listes vide pour stocker les distributions de cartes
        for _ in range(nb_cartes):  # Répète le processus pour le nombre de cartes spécifié
            for i in range(nb_joueurs):  # Parcourt les joueurs
                carte = self.piocher()  # Pioche une carte du paquet
                distributions[i].append(carte)  # Ajoute la carte à la distribution du joueur correspondant
        return distributions  # Retourne les distributions de cartes

