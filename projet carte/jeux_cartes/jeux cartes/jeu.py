from joueur import Joueur  # Importe la classe Joueur depuis le module joueur
from paquet import Paquet  # Importe la classe Paquet depuis le module paquet

class Jeu:
    def __init__(self, joueurs):
        self.joueurs = [Joueur(nom) for nom in joueurs]  # Crée une liste de joueurs en utilisant la classe Joueur
        self.paquet = Paquet()  # Crée une instance de la classe Paquet
        self.pli_en_cours = []  # Initialise une liste vide pour le pli en cours
        self.couleur_demandee = None  # Initialise la couleur demandée à None

    def demarrer(self):
        self.paquet.melanger()  # Mélange le paquet de cartes
        self.distribuer_cartes(8)  # Distribue 8 cartes à chaque joueur

    def distribuer_cartes(self, nb_cartes_par_joueur):
        distributions = self.paquet.distribuer(len(self.joueurs), nb_cartes_par_joueur)  # Distribue les cartes du paquet aux joueurs
        for joueur, main in zip(self.joueurs, distributions):
            joueur.main = main  # Attribue la main distribuée à chaque joueur

    def afficher_mains_joueurs(self):
        for joueur in self.joueurs:
            joueur.afficher_main()  # Affiche la main de chaque joueur

    def tour_suivant(self):
        for joueur in self.joueurs:
            carte = joueur.jouer_carte(self.couleur_demandee)  # Chaque joueur joue une carte en fonction de la couleur demandée
            print(f"Le joueur {joueur.nom} joue : {carte}")  # Affiche la carte jouée par chaque joueur
            self.pli_en_cours.append((joueur, carte))  # Ajoute la paire (joueur, carte) au pli en cours

        self.pli_en_cours.sort(key=lambda pair: pair[1].points(), reverse=True)  # Trie le pli en cours en fonction des points des cartes
        gagnant = self.pli_en_cours[0][0]  # Récupère le joueur gagnant du pli
        print(f"Pli remporté par : {gagnant.nom}")  # Affiche le nom du joueur gagnant

        joueur_gagnant = next(joueur for joueur, carte in self.pli_en_cours if carte == self.pli_en_cours[0][1])  # Récupère le joueur gagnant du pli en fonction de la carte gagnante
        joueur_gagnant.ramasser_pli([pair[1] for pair in self.pli_en_cours])  # Le joueur gagnant ramasse le pli
        self.pli_en_cours = []  # Réinitialise le pli en cours

    def terminer_partie(self):
        print("\nFin de la partie.")
        points_joueurs = [(joueur.nom, joueur.calculer_points()) for joueur in self.joueurs]  # Calcule les points de chaque joueur
        points_joueurs.sort(key=lambda x: x[1])  # Trie les joueurs en fonction de leurs points
        print("Classement final :")
        for i, (nom, points) in enumerate(points_joueurs, start=1):
            print(f"{i}. {nom} - {points} points")  # Affiche le classement final des joueurs avec leurs points
