#Auteur:Raphael Gonzalez Carvajal
#Date:12 mars 2021

#Le programme suivant fera un jeu de vie où les cellules dans une grille
#changeront de couleur selon un ensembles de règles données

# FUNCTIONS ###################################################################

#Fonction qui transforme position 1D de cellule en position 2D
def posMatrix(tailleGrille):
    posTab=[]
    for item in grille.posInitVivant:
        pos=[]
        if item%tailleGrille.nx==0:
            colone=tailleGrille.nx
        else:
            colone=item%tailleGrille.nx
        ligne=math.ceil(item/tailleGrille.nx)
        ligne=int(ligne)
        pos.append(ligne);pos.append(colone)
        posTab.append(pos)
    return posTab

#Fonction qui déssine une cellule
def carre(largeur):
    for _ in range(4):
        fd(largeur)
        rt(90)
    fd(largeur)

#Fonction qui fait passer la tortue à la prochaine ligne
def ligneSuivante(largeur,nx):
    rt(90);fd(largeur);rt(90)
    fd(largeur*nx);rt(180)
    
#Fonction pour creer un grillage
def creerGrille(tailleGrille):
    #tailleGrille est struct(nx,ny,largeur)
    #px et py permettent de garder la grille relativement centré
    px = -tailleGrille.nx*tailleGrille.largeur/2
    py = tailleGrille.ny*tailleGrille.largeur/2
    pu(); goto(px,py); pd()
    #Boucle pour la grille
    for _ in range(tailleGrille.ny):
        for _ in range(tailleGrille.nx):
            carre(tailleGrille.largeur)
        ligneSuivante(tailleGrille.largeur, tailleGrille.nx)
        
#Création de l'état initiale du modèle
def init(grille): 
    #grille: posInitVivant(list),initVivant(int))
    nbCellules = tailleGrille.nx*tailleGrille.ny
    #Boucle pour trouver le nombre de cellules vivantes
    while True:
        initVivant = round(nbCellules*random())
        if (initVivant>=0.10*nbCellules) and (initVivant<=0.5*nbCellules):
            break
        else:
            continue
    #Création d'une liste contenant position de case vivante
    for _ in range(initVivant):
        grille.posInitVivant.append(round(nbCellules*random()))
    grille.posInitVivant=posMatrix(tailleGrille)
    
#Fonction qui dessine les cases
def dessinerGrille(tailleGrille,grille):
    #(px,py) correspond au coin supérieure gauche de la grille
    px = -tailleGrille.nx*tailleGrille.largeur/2
    py = tailleGrille.ny*tailleGrille.largeur/2
    
    #dessin de l'intérieure des cellules
    goto(px,py-5); pu()
    pensize(tailleGrille.largeur)
    pencolor(1,0,0)
    for cell in grille.posInitVivant:
        if cell[0]==0:
            continue
        else:
            goto(px,py+5-cell[0]*tailleGrille.largeur)
            fd((cell[1]-1)*tailleGrille.largeur);pd();fd(tailleGrille.largeur);pu()
            goto(px,py-5)

#Fonction pour calculer le prochain état du tableau
def prochainEtat(grille,tailleGrille):
    #création de toutes les cases que nous allons tester
    test=[]
    for i in range(1,tailleGrille.nx+1):
        for j in range(1,tailleGrille.ny+1):
            test.append([i,j])
    #compter le nombre de voisins Vivants d'une cellule
    for cell in test:
        voisinVivant=0
        while voisinVivant<=3:
            if [cell[0]-1,cell[1]-1] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0]-1,cell[1]] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0]-1,cell[1]+1] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0],cell[1]-1] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0],cell[1]+1] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0]+1,cell[1]-1] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0]+1,cell[1]] in grille.posInitVivant:
                voisinVivant+=1
            if [cell[0]+1,cell[1]+1] in grille.posInitVivant:
                voisinVivant+=1
            break
        #Différencie les cases vivantes des mortes dans le test
        if cell in grille.posInitVivant:
            if voisinVivant==2 or voisinVivant==3:
                grille.posFutureVivant.append(cell)
        if cell not in grille.posInitVivant:
            if voisinVivant==3:
                grille.posFutureVivant.append(cell)

#Fonction qui fait rouler le jeu
def jouer(tailleGrille):
    creerGrille(tailleGrille)
    init(grille)
    dessinerGrille(tailleGrille,grille)
    #Début du jeu
    while True:
        prochainEtat(grille,tailleGrille)
        grille.posInitVivant=grille.posFutureVivant
        grille.posFutureVivant=[]
        if grille.posInitVivant==[]:
            break
        sleep(0.1)
        clear()
        creerGrille(tailleGrille)
        dessinerGrille(tailleGrille,grille)
        
# MAIN ########################################################################
        
#Structures de données
tailleGrille = struct(nx=20,ny=20,largeur=10)
grille = struct(posInitVivant = [],posFutureVivant=[], initVivant = 0)

jouer(tailleGrille)






























