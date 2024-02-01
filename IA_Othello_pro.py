# Importation des bibliothèques
from tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy

# Configuration des variables
noeuds = 0
profondeur = 4
coups = 0

# Configuration de Tkinter
racine = Tk()
ecran = Canvas(racine, width=500, height=600, background="#222", highlightthickness=0)
ecran.pack()


class Plateau:
    def __init__(self):
        # Le joueur blanc commence en premier (0 est blanc et joueur, 1 est noir et ordinateur)
        self.joueur = 0
        self.passe = False
        self.gagne = False
        # Initialisation d'un plateau vide
        self.tableau = []
        for x in range(8):
            self.tableau.append([])
            for y in range(8):
                self.tableau[x].append(None)

        # Initialisation des valeurs au centre
        self.tableau[3][3] = "w"
        self.tableau[3][4] = "b"
        self.tableau[4][3] = "b"
        self.tableau[4][4] = "w"

        # Initialisation des anciennes valeurs
        self.tableau_prec = self.tableau

    # Mise à jour du plateau sur l'écran
    def mise_a_jour(self):
        ecran.delete("animation")
        ecran.delete("tuile")
        for x in range(8):
            for y in range(8):
                # Pourrait remplacer les cercles par des images plus tard, si nécessaire
                if self.tableau_prec[x][y] == "w":
                    ecran.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x, 96 + 50 * y,
                                      tags="tuile {0}-{1}".format(x, y), fill="#aaa", outline="#aaa")
                    ecran.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x, 94 + 50 * y,
                                      tags="tuile {0}-{1}".format(x, y), fill="#fff", outline="#fff")

                elif self.tableau_prec[x][y] == "b":
                    ecran.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x, 96 + 50 * y,
                                      tags="tuile {0}-{1}".format(x, y), fill="#000", outline="#000")
                    ecran.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x, 94 + 50 * y,
                                      tags="tuile {0}-{1}".format(x, y), fill="#111", outline="#111")

        # Animation des nouvelles tuiles
        ecran.update()
        for x in range(8):
            for y in range(8):
                # Pourrait remplacer les cercles par des images plus tard, si nécessaire
                if self.tableau[x][y] != self.tableau_prec[x][y] and self.tableau[x][y] == "w":
                    ecran.delete("{0}-{1}".format(x, y))
                    # 42 est la largeur de la tuile donc 21 est la moitié de cela
                    # Rétrécissement
                    for i in range(21):
                        ecran.create_oval(54 + i + 50 * x, 54 + i + 50 * y, 96 - i + 50 * x, 96 - i + 50 * y,
                                          tags="tuile animee", fill="#000", outline="#000")
                        ecran.create_oval(54 + i + 50 * x, 52 + i + 50 * y, 96 - i + 50 * x, 94 - i + 50 * y,
                                          tags="tuile animee", fill="#111", outline="#111")
                        if i % 3 == 0:
                            sleep(0.01)
                        ecran.update()
                        ecran.delete("animee")
                    # Croissance
                    for i in reversed(range(21)):
                        ecran.create_oval(54 + i + 50 * x, 54 + i + 50 * y, 96 - i + 50 * x, 96 - i + 50 * y,
                                          tags="tuile animee", fill="#aaa", outline="#aaa")
                        ecran.create_oval(54 + i + 50 * x, 52 + i + 50 * y, 96 - i + 50 * x, 94 - i + 50 * y,
                                          tags="tuile animee", fill="#fff", outline="#fff")
                        if i % 3 == 0:
                            sleep(0.01)
                        ecran.update()
                        ecran.delete("animee")
                    ecran.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x, 96 + 50 * y, tags="tuile", fill="#aaa",
                                      outline="#aaa")
                    ecran.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x, 94 + 50 * y, tags="tuile", fill="#fff",
                                      outline="#fff")
                    ecran.update()

                elif self.tableau[x][y] != self.tableau_prec[x][y] and self.tableau[x][y] == "b":
                    ecran.delete("{0}-{1}".format(x, y))
                    # 42 est la largeur de la tuile donc 21 est la moitié de cela
                    # Rétrécissement
                    for i in range(21):
                        ecran.create_oval(54 + i + 50 * x, 54 + i + 50 * y, 96 - i + 50 * x, 96 - i + 50 * y,
                                          tags="tuile animee", fill="#aaa", outline="#aaa")
                        ecran.create_oval(54 + i + 50 * x, 52 + i + 50 * y, 96 - i + 50 * x, 94 - i + 50 * y,
                                          tags="tuile animee", fill="#fff", outline="#fff")
                        if i % 3 == 0:
                            sleep(0.01)
                        ecran.update()
                        ecran.delete("animee")
                    # Croissance
                    for i in reversed(range(21)):
                        ecran.create_oval(54 + i + 50 * x, 54 + i + 50 * y, 96 - i + 50 * x, 96 - i + 50 * y,
                                          tags="tuile animee", fill="#000", outline="#000")
                        ecran.create_oval(54 + i + 50 * x, 52 + i + 50 * y, 96 - i + 50 * x, 94 - i + 50 * y,
                                          tags="tuile animee", fill="#111", outline="#111")
                        if i % 3 == 0:
                            sleep(0.01)
                        ecran.update()
                        ecran.delete("animee")

                    ecran.create_oval(54 + 50 * x, 54 + 50 * y, 96 + 50 * x, 96 + 50 * y, tags="tuile", fill="#000",
                                      outline="#000")
                    ecran.create_oval(54 + 50 * x, 52 + 50 * y, 96 + 50 * x, 94 + 50 * y, tags="tuile", fill="#111",
                                      outline="#111")
                    ecran.update()

        # Dessin des cercles de mise en évidence
        for x in range(8):
            for y in range(8):
                if self.joueur == 0:
                    if valide(self.tableau, self.joueur, x, y):
                        ecran.create_oval(68 + 50 * x, 68 + 50 * y, 32 + 50 * (x + 1), 32 + 50 * (y + 1),
                                          tags="animation", fill="#008000", outline="#008000")

        if not self.gagne:
            # Dessine le tableau des scores et met à jour l'écran
            self.dessiner_tableau_scores()
            ecran.update()
            # Si l'ordinateur est une IA, effectuer un mouvement
            if self.joueur == 1:
                temps_depart = time()
                self.tableau_prec = self.tableau
                resultat_alpha_beta = self.alphaBeta(self.tableau, profondeur, -float("inf"), float("inf"), 1)
                self.tableau = resultat_alpha_beta[1]

                if len(resultat_alpha_beta) == 3:
                    position = resultat_alpha_beta[2]
                    self.tableau_prec[position[0]][position[1]] = "b"

                self.joueur = 1 - self.joueur
                delta_temps = round((time() - temps_depart) * 100) / 100
                if delta_temps < 2:
                    sleep(2 - delta_temps)
                noeuds = 0
                # Le joueur doit-il passer ?
                self.test_passe()
        else:
            ecran.create_text(250, 550, anchor="c", font=("Consolas", 15), text="Le jeu est terminé!")

    # Déplacement vers une position
    def deplacer_plateau(self, x, y):
        global noeuds
        # Déplacement et mise à jour de l'écran
        self.tableau_prec = self.tableau
        self.tableau_prec[x][y] = "w"
        self.tableau = deplacer(self.tableau, x, y)

        # Changement de joueur
        self.joueur = 1 - self.joueur
        self.mise_a_jour()

        # Vérifier si l'IA doit passer
        self.test_passe()
        self.mise_a_jour()

    # METHODE: Dessine le tableau des scores à l'écran
    def dessiner_tableau_scores(self):
        global coups
        # Suppression des éléments de score précédents
        ecran.delete("score")

        # Attribution de points en fonction du nombre de tuiles
        score_joueur = 0
        score_ordinateur = 0
        for x in range(8):
            for y in range(8):
                if self.tableau[x][y] == "w":
                    score_joueur += 1
                elif self.tableau[x][y] == "b":
                    score_ordinateur += 1

        if self.joueur == 0:
            couleur_joueur = "green"
            couleur_ordinateur = "gray"
        else:
            couleur_joueur = "gray"
            couleur_ordinateur = "green"

        ecran.create_oval(5, 540, 25, 560, fill=couleur_joueur, outline=couleur_joueur)
        ecran.create_oval(380, 540, 400, 560, fill=couleur_ordinateur, outline=couleur_ordinateur)

        # Ajout de texte à l'écran
        ecran.create_text(30, 550, anchor="w", tags="score", font=("Consolas", 50), fill="white", text=score_joueur)
        ecran.create_text(400, 550, anchor="w", tags="score", font=("Consolas", 50), fill="black",
                          text=score_ordinateur)

        coups = score_joueur + score_ordinateur

    # METHODE: Teste si le joueur doit passer : s'il le doit, change de joueur
    def test_passe(self):
        doit_passer = True
        for x in range(8):
            for y in range(8):
                if valide(self.tableau, self.joueur, x, y):
                    doit_passer = False
        if doit_passer:
            self.joueur = 1 - self.joueur
            if self.passe == True:
                self.gagne = True
            else:
                self.passe = True
            self.mise_a_jour()
        else:
            self.passe = False

    # METHODE: IA stupide - Choix d'un déplacement aléatoire
    def deplacement_stupide(self):
        # Génère tous les déplacements possibles
        choix = []
        for x in range(8):
            for y in range(8):
                if valide(self.tableau, self.joueur, x, y):
                    choix.append([x, y])
        # Choix d'un déplacement aléatoire, se déplace là-bas
        deplacement_stupide = choice(choix)
        self.deplacer_plateau(deplacement_stupide[0], deplacement_stupide[1])

    # METHODE: IA pas si stupide - Choix d'un déplacement basé sur ce qui obtiendra le plus de pièces au prochain tour
    def deplacement_un_peu_moins_stupide(self):
        # Génère tous les choix possibles et les plateaux correspondants
        plateaux = []
        choix = []
        for x in range(8):
            for y in range(8):
                if valide(self.tableau, self.joueur, x, y):
                    test = self.deplacer(self.tableau, x, y)
                    plateaux.append(test)
                    choix.append([x, y])

        # Détermine le meilleur score en fonction des plateaux générés précédemment et d'une heuristique "Dumb" : dumbScore()
        meilleur_score = -float("inf")
        meilleur_indice = 0
        for i in range(len(plateaux)):
            score = self.scoreSimple(plateaux[i], self.joueur)
            if score > meilleur_score:
                meilleur_indice = i
                meilleur_score = score
        # Se déplace vers le meilleur emplacement en fonction de dumbScore()
        self.deplacer_plateau(choix[meilleur_indice][0], choix[meilleur_indice][1])

    # METHODE: IA Réellement Décente - Choix d'un déplacement basé sur une heuristique simple
    # Identique à slightlyLessDumbMove(), utilise simplement slightlyLessDumbScore()
    def deplacement_decent(self):
        # Génère tous les choix possibles et les plateaux correspondants
        plateaux = []
        choix = []
        for x in range(8):
            for y in range(8):
                if self.valide(self.tableau, self.joueur, x, y):
                    test = deplacer(self.tableau, x, y)
                    plateaux.append(test)
                    choix.append([x, y])

        meilleur_score = -float("inf")
        meilleur_indice = 0
        # Détermine le meilleur score en fonction des plateaux générés précédemment et d'une heuristique "Meh" : slightlyLessDumbScore()
        for i in range(len(plateaux)):
            score = self.scoreMoinsSimple(plateaux[i], self.joueur)
            if score > meilleur_score:
                meilleur_indice = i
                meilleur_score = score
        # Se déplace vers le meilleur emplacement en fonction de slightlyLessDumbScore()
        self.deplacer_plateau(choix[meilleur_indice][0], choix[meilleur_indice][1])

    # Cette section contient l'algorithme minimax

    def minimax(self, noeud, profondeur, maximisation):
        global noeuds
        noeuds += 1
        plateaux = []
        choix = []

        for x in range(8):
            for y in range(8):
                if self.valide(self.tableau, self.joueur, x, y):
                    test = deplacer(noeud, x, y)
                    plateaux.append(test)
                    choix.append([x, y])

        if profondeur == 0 or len(choix) == 0:
            return ([self.heuristique_decente(noeud, 1 - maximisation), noeud])

        if maximisation:
            meilleure_valeur = -float("inf")
            meilleur_plateau = []
            for plateau in plateaux:
                val = self.minimax(plateau, profondeur - 1, 0)[0]
                if val > meilleure_valeur:
                    meilleure_valeur = val
                    meilleur_plateau = plateau
            return ([meilleure_valeur, meilleur_plateau])

        else:
            meilleure_valeur = float("inf")
            meilleur_plateau = []
            for plateau in plateaux:
                val = self.minimax(plateau, profondeur - 1, 1)[0]
                if val < meilleure_valeur:
                    meilleure_valeur = val
                    meilleur_plateau = plateau
            return ([meilleure_valeur, meilleur_plateau])

    # Élagage alpha-bêta sur l'arbre minimax

    def alphaBeta(self, noeud, profondeur, alpha, beta, maximisation):
        global noeuds
        noeuds += 1
        plateaux = []
        choix = []

        for x in range(8):
            for y in range(8):
                if valide(self.tableau, self.joueur, x, y):
                    test = deplacer(noeud, x, y)
                    plateaux.append(test)
                    choix.append([x, y])

        if profondeur == 0 or len(choix) == 0:
            return ([heuristiqueFinale(noeud, maximisation), noeud])

        if maximisation:
            v = -float("inf")
            meilleur_plateau = []
            meilleur_choix = []
            for plateau in plateaux:
                valeur_plateau = self.alphaBeta(plateau, profondeur - 1, alpha, beta, 0)[0]
                if valeur_plateau > v:
                    v = valeur_plateau
                    meilleur_plateau = plateau
                    meilleur_choix = choix[plateaux.index(plateau)]
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return ([v, meilleur_plateau, meilleur_choix])
        else:
            v = float("inf")
            meilleur_plateau = []
            meilleur_choix = []
            for plateau in plateaux:
                valeur_plateau = self.alphaBeta(plateau, profondeur - 1, alpha, beta, 1)[0]
                if valeur_plateau < v:
                    v = valeur_plateau
                    meilleur_plateau = plateau
                    meilleur_choix = choix[plateaux.index(plateau)]
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return ([v, meilleur_plateau, meilleur_choix])


# FONCTION: Retourne un plateau après avoir effectué un déplacement selon les règles d'Othello
# Suppose que le déplacement est valide
def deplacer(tableau_passe, x, y):
    # Doit copier le tableau_passe pour ne pas altérer l'original
    tableau = deepcopy(tableau_passe)
    # Définir la couleur et définir l'emplacement déplacé à cette couleur
    if plateau.joueur == 0:
        couleur = "w"

    else:
        couleur = "b"
    tableau[x][y] = couleur

    # Détermination des voisins de la case
    voisins = []
    for i in range(max(0, x - 1), min(x + 2, 8)):
        for j in range(max(0, y - 1), min(y + 2, 8)):
            if tableau[i][j] != None:
                voisins.append([i, j])

    # Quelles tuiles convertir
    convertir = []

    # Pour tous les voisins générés, déterminer s'ils forment une ligne
    # Si une ligne est formée, nous l'ajouterons au tableau de conversion
    for voisin in voisins:
        voisinX = voisin[0]
        voisinY = voisin[1]
        # Vérifier si le voisin est d'une couleur différente - il doit l'être pour former une ligne
        if tableau[voisinX][voisinY] != couleur:
            # Le chemin de chaque ligne individuelle
            chemin = []

            # Détermination de la direction à suivre
            deltaX = voisinX - x
            deltaY = voisinY - y

            tempX = voisinX
            tempY = voisinY

            # Tant que nous sommes dans les limites du tableau
            while 0 <= tempX <= 7 and 0 <= tempY <= 7:
                chemin.append([tempX, tempY])
                valeur = tableau[tempX][tempY]
                # Si nous atteignons une case vide, c'est terminé et il n'y a pas de ligne
                if valeur == None:
                    break
                # Si nous atteignons une case de la couleur du joueur, une ligne est formée
                if valeur == couleur:
                    # Ajouter tous les nœuds de notre chemin au tableau de conversion
                    for node in chemin:
                        convertir.append(node)
                    break
                # Déplacer la tuile
                tempX += deltaX
                tempY += deltaY

    # Convertir toutes les tuiles appropriées
    for node in convertir:
        tableau[node[0]][node[1]] = couleur

    return tableau


# Fonction pour dessiner les lignes de la grille
def dessinerGrilleBackground(contour=False):
    # Si nous voulons un contour sur le plateau, dessinez-en un
    if contour:
        ecran.create_rectangle(50, 50, 450, 450, outline="#111")

    # Dessin des lignes intermédiaires
    for i in range(7):
        decalageLigne = 50 + 50 * (i + 1)

        # Ligne horizontale
        ecran.create_line(50, decalageLigne, 450, decalageLigne, fill="#111")

        # Ligne verticale
        ecran.create_line(decalageLigne, 50, decalageLigne, 450, fill="#111")

    ecran.update()


# Heuristique simple. Compare le nombre de chaque tuile.
def scoreSimple(tableau, joueur):
    score = 0
    # Définir la couleur du joueur et de l'adversaire
    if joueur == 1:
        couleur = "b"
        adversaire = "w"
    else:
        couleur = "w"
        adversaire = "b"
    # +1 s'il s'agit de la couleur du joueur, -1 s'il s'agit de la couleur de l'adversaire
    for x in range(8):
        for y in range(8):
            if tableau[x][y] == couleur:
                score += 1
            elif tableau[x][y] == adversaire:
                score -= 1
    return score


# Heuristique un peu moins simple mais toujours simple. Pèse les coins et les bords davantage
def scoreMoinsSimple(tableau, joueur):
    score = 0
    # Définir la couleur du joueur et de l'adversaire
    if joueur == 1:
        couleur = "b"
        adversaire = "w"
    else:
        couleur = "w"
        adversaire = "b"
    # Parcourir toutes les tuiles
    for x in range(8):
        for y in range(8):
            # Les tuiles normales valent 1
            ajout = 1
            # Les tuiles du bord valent 3
            if (x == 0 and 1 < y < 6) or (x == 7 and 1 < y < 6) or (y == 0 and 1 < x < 6) or (y == 7 and 1 < x < 6):
                ajout = 3
            # Les tuiles de coin valent 5
            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                ajout = 5
            # Ajouter ou soustraire la valeur de la tuile correspondant à la couleur
            if tableau[x][y] == couleur:
                score += ajout
            elif tableau[x][y] == adversaire:
                score -= ajout
    return score


# Heuristique qui pondère les tuiles de coin et de bord comme positives, les tuiles adjacentes aux coins (si le coin n'est pas le vôtre) comme négatives
# Pondère les autres tuiles comme un point
def heuristiqueCorrecte(tableau, joueur):
    score = 0
    valeurCoin = 25
    valeurAdjacent = 5
    valeurBord = 5
    # Définir la couleur du joueur et de l'adversaire
    if joueur == 1:
        couleur = "b"
        adversaire = "w"
    else:
        couleur = "w"
        adversaire = "b"
    # Parcourir toutes les tuiles
    for x in range(8):
        for y in range(8):
            # Les tuiles normales valent 1
            ajout = 1

            # Adjacent aux coins vaut -3
            if (x == 0 and y == 1) or (x == 1 and 0 <= y <= 1):
                if tableau[0][0] == couleur:
                    ajout = valeurBord
                else:
                    ajout = -valeurAdjacent

            elif (x == 0 and y == 6) or (x == 1 and 6 <= y <= 7):
                if tableau[7][0] == couleur:
                    ajout = valeurBord
                else:
                    ajout = -valeurAdjacent

            elif (x == 7 and y == 1) or (x == 6 and 0 <= y <= 1):
                if tableau[0][7] == couleur:
                    ajout = valeurBord
                else:
                    ajout = -valeurAdjacent

            elif (x == 7 and y == 6) or (x == 6 and 6 <= y <= 7):
                if tableau[7][7] == couleur:
                    ajout = valeurBord
                else:
                    ajout = -valeurAdjacent

            # Les tuiles de bord valent 3
            elif (x == 0 and 1 < y < 6) or (x == 7 and 1 < y < 6) or (y == 0 and 1 < x < 6) or (y == 7 and 1 < x < 6):
                ajout = valeurBord
            # Les tuiles de coin valent 15
            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                ajout = valeurCoin
            # Ajouter ou soustraire la valeur de la tuile correspondant à la couleur
            if tableau[x][y] == couleur:
                score += ajout
            elif tableau[x][y] == adversaire:
                score -= ajout
    return score


# Séparation de l'utilisation des heuristiques pour le début/milieu/fin de partie.
def heuristiqueFinale(tableau, joueur):
    if coups <= 8:
        numMoves = 0
        for x in range(8):
            for y in range(8):
                if valide(tableau, joueur, x, y):
                    numMoves += 1
        return numMoves + heuristiqueCorrecte(tableau, joueur)
    elif coups <= 52:
        return heuristiqueCorrecte(tableau, joueur)
    elif coups <= 58:
        return scoreMoinsSimple(tableau, joueur)
    else:
        return scoreSimple(tableau, joueur)


# Vérifie si un déplacement est valide pour un tableau donné.
def valide(tableau, joueur, x, y):
    # Définit la couleur du joueur
    if joueur == 0:
        couleur = "w"
    else:
        couleur = "b"

    # S'il y a déjà une pièce à cet endroit, c'est un mouvement invalide
    if tableau[x][y] is not None:
        return False
    else:
        # Génération de la liste des voisins
        voisin = False
        voisins = []
        for i in range(max(0, x - 1), min(x + 2, 8)):
            for j in range(max(0, y - 1), min(y + 2, 8)):
                if tableau[i][j] is not None:
                    voisin = True
                    voisins.append([i, j])
        # S'il n'y a pas de voisins, c'est un mouvement invalide
        if not voisin:
            return False
        else:
            # Itération à travers les voisins pour déterminer si au moins une ligne est formée
            valide = False
            for voisin in voisins:

                neighX = voisin[0]
                neighY = voisin[1]

                # Si la couleur du voisin est égale à votre couleur, cela ne forme pas de ligne
                # Passez au voisin suivant
                if tableau[neighX][neighY] == couleur:
                    continue
                else:
                    # Déterminer la direction de la ligne
                    deltaX = neighX - x
                    deltaY = neighY - y
                    tempX = neighX
                    tempY = neighY

                    while 0 <= tempX <= 7 and 0 <= tempY <= 7:
                        # S'il y a un espace vide, aucune ligne n'est formée
                        if tableau[tempX][tempY] is None:
                            break
                        # S'il atteint une pièce de la couleur du joueur, cela forme une ligne
                        if tableau[tempX][tempY] == couleur:
                            valide = True
                            break
                        # Déplacez l'index en fonction de la direction de la ligne
                        tempX += deltaX
                        tempY += deltaY
            return valide


# Lorsque l'utilisateur clique, s'il s'agit d'un mouvement valide, effectuez le mouvement
def gestionClic(event):
    global depth
    xSouris = event.x
    ySouris = event.y
    if running:
        if xSouris >= 450 and ySouris <= 50:
            racine.destroy()
        elif xSouris <= 50 and ySouris <= 50:
            jouerPartie()
        else:
            # Est-ce le tour du joueur ?
            if plateau.joueur == 0:
                # Supprimer les points saillants
                x = int((event.x - 50) / 50)
                y = int((event.y - 50) / 50)
                # Déterminer l'index de la grille pour l'endroit où la souris a été cliquée

                # Si le clic est à l'intérieur des limites et que le déplacement est valide, déplacez-vous à cet endroit
                if 0 <= x <= 7 and 0 <= y <= 7:
                    if valide(plateau.tableau, plateau.joueur, x, y):
                        plateau.deplacer_plateau(x, y)
    else:
        # Difficulté de clic
        if 300 <= ySouris <= 350:
            # Une étoile
            if 25 <= xSouris <= 155:
                depth = 1
                jouerPartie()
            # Deux étoiles
            elif 180 <= xSouris <= 310:
                depth = 4
                jouerPartie()
            # Trois étoiles
            elif 335 <= xSouris <= 465:
                depth = 6
                jouerPartie()


def gestionClavier(event):
    symbole = event.keysym
    if symbole.lower() == "r":
        jouerPartie()
    elif symbole.lower() == "q":
        racine.destroy()


def creer_boutons():
    # Bouton de redémarrage
    # Arrière-plan/ombre
    ecran.create_rectangle(0, 5, 50, 55, fill="#000033", outline="#000033")
    ecran.create_rectangle(0, 0, 50, 50, fill="#000088", outline="#000088")

    # Flèche
    ecran.create_arc(5, 5, 45, 45, fill="#000088", width="2", style="arc", outline="white", extent=300)
    ecran.create_polygon(33, 38, 36, 45, 40, 39, fill="white", outline="white")

    # Bouton Quitter
    # Arrière-plan/ombre
    ecran.create_rectangle(450, 5, 500, 55, fill="#330000", outline="#330000")
    ecran.create_rectangle(450, 0, 500, 50, fill="#880000", outline="#880000")
    # "X"
    ecran.create_line(455, 5, 495, 45, fill="white", width="3")
    ecran.create_line(495, 5, 455, 45, fill="white", width="3")


def executerPartie():
    global running
    running = False
    # Titre et ombre
    ecran.create_text(250, 203, anchor="c", text="Othello", font=("Consolas", 50), fill="#aaa")
    ecran.create_text(250, 200, anchor="c", text="Othello", font=("Consolas", 50), fill="#fff")

    # Création des boutons de difficulté
    for i in range(3):
        # Arrière-plan
        ecran.create_rectangle(25 + 155 * i, 310, 155 + 155 * i, 355, fill="#000", outline="#000")
        ecran.create_rectangle(25 + 155 * i, 300, 155 + 155 * i, 350, fill="#111", outline="#111")

        espacement = 130 / (i + 2)
        for x in range(i + 1):
            # Étoile avec double ombre
            ecran.create_text(25 + (x + 1) * espacement + 155 * i, 326, anchor="c", text="\u2605",
                              font=("Consolas", 25), fill="#b29600")
            ecran.create_text(25 + (x + 1) * espacement + 155 * i, 327, anchor="c", text="\u2605",
                              font=("Consolas", 25), fill="#b29600")
            ecran.create_text(25 + (x + 1) * espacement + 155 * i, 325, anchor="c", text="\u2605",
                              font=("Consolas", 25), fill="#ffd700")

    ecran.update()


def jouerPartie():
    global plateau, running
    running = True
    ecran.delete(ALL)
    creer_boutons()
    plateau = 0

    # Dessiner l'arrière-plan
    dessinerGrilleBackground()

    # Créer le plateau et le mettre à jour
    plateau = Plateau()
    plateau.mise_a_jour()


jouerPartie()

# Liaison, configuration
ecran.bind("<Button-1>", gestionClic)
ecran.bind("<Key>", gestionClavier)
ecran.focus_set()

# Exécuter indéfiniment
racine.wm_title("Othello")
racine.mainloop()
