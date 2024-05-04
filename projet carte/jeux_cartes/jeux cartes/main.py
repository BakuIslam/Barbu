from jeu import Jeu  # Importe la classe Jeu depuis le module jeu



def main():
    joueurs = ["Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4"]  # Liste des noms des joueurs
    jeu = Jeu(joueurs)  # Crée une instance de la classe Jeu avec les joueurs
    jeu.demarrer()  # Démarre le jeu

    while True:  # Boucle infinie
        jeu.tour_suivant()  # Passe au tour suivant
        continuer = input("  continuer la partie  ?   ")  # Demande à l'utilisateur s'il souhaite continuer
        if continuer.lower() != "oui":  # Si la réponse n'est pas "oui"
            break  # Sort de la boucle

    jeu.terminer_partie()  # Termine la partie

main()  # Appelle la fonction main si le script est exécuté directement

