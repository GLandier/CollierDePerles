#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from turtle import*
from math import*
from random import*
from random import choice

def signature():
    width(3)
    #Ecriture du G
    down()
    left(180)
    forward(80)
    left(90)
    forward(80)
    left(90)
    forward(80)
    left(90)
    forward(40)
    left(90)
    forward(40)
    # je refais la barre du G a l'envers pour que la turtle puisse faire l'espace
    up()
    right(180)
    forward(40)
    right(90)
    forward(40)
    left(90)
    # espace
    forward(20)
    #Ecriture du A
    down()
    left(60)
    forward(95)
    right(120)
    forward(95)
    backward(45)
    right(120)
    forward(50)
    # je refais le chemin du A a l'envers pour que la turtle puisse faire l'espace
    up()
    backward(50)
    left(120)
    forward(45)
    left(60)
    #espace
    forward(20)
    #Ecriture L
    down()
    forward(60)
    backward(60)
    left(90)
    forward(80)
    # je refais le chemin du L a l'envers pour que la turtle puisse faire l'espace
    up()
    backward(80)
    right(90)
    #espace
    forward(80)
     #Ecriture du A
    down()
    left(60)
    forward(95)
    right(120)
    forward(95)
    backward(45)
    right(120)
    forward(50)
    #ajout du sourire
    #je recule de moitié de la barre du A
    up()
    backward(25)
    left(90)
    forward(10)
    down()
    left(180)
    circle(98,-180)
    left(180)

def perleA(r,rcouleur):
    down()
    # je trace le cercle exterieur du carré
    circle(r,360)
    #Tracage du carré
    left(90)
    up()
    forward(r/2)#je remonte de la moitié du rayon pour pouvoir tracer le cercle
    down()
    fillcolor(rcouleur)# je donne de la couleur au carré
    begin_fill()
    left(45)
    forward(sqrt((r/2)**2+(r/2)**2))#je fais le theorème de Pytagore pour tracer le coté du carré
    for i in range (4):#je trace 3 fois le coté du carré avec un angle de 90 degre
        right(90)
        forward(sqrt((r/2)**2+(r/2)**2))
    end_fill()
    #repositionement de la turtle et haut du cercle extérieur
    up()
    right(90)
    forward(sqrt((r/2)**2+(r/2)**2))
    left(45)
    forward(r/2)
    right(90)

def perleB(r,rcouleur):
    down()
    circle(r,360)# je fais le cercle exterieur
    #Tracage de la goute
    left(90)
    up()
    forward(r)
    down()
    fillcolor(rcouleur)# je donne de la couleur a la goute
    begin_fill()
    up()
    left(90)
    forward(r/4)#je me déplace d'un quart de rayon en partant du centre
    down()
    left(90)
    circle(r/4,180)#je trace un demi cercle qui sera le bas de la goute
    left(30)#je tourne de 30 degres pour tracé un triangle qui sera le haut de la goute
    forward(r/2)# le coté du carré est d'un demi rayon
    left(120)# le coté du carré est d'un demi rayon
    forward(r/2)#je tourne de 30 degres pour tracé un triangle qui sera le haut de la goute
    end_fill()
    #repositionement de la turtle en haut du cercle pour continuer
    up()
    backward(r/2)
    right(120)
    backward(r/2)
    right(30)
    left(90)
    forward(r/4)
    right(90)
    forward(r)
    right(90)

def perleC(r,rcouleur,n):
    down()
    circle(r,360)
    #tracage des cercle à l'interieur
    x=0#x est un variable qui ermet de definir la couleur du cercle interieur selon si x est paire ou impaire
    rc=r-(r/n)# rc est le rayon du cercle intérieur. Il est calculé en enlevent au rayon de la perle le rayon de la perle divisé a le nombre de cercle
    for i in range(1,n+1):#je crée une boucle tracer autant de cercle que n
        up()
        left(90)
        forward(r/n)# j'avance du rayon divisé par n
        right(90)
        if x%2==0:# si x est paire, le cercle sera coloré
            begin_fill()
            fillcolor(rcouleur)
            down()
            circle(rc,360)
            up()
            end_fill()
            x=x+1#on ajoute 1 a x a chaque répétition
            rc=rc-(r/n)#on refix rc pour que les cercles soit de plus en plus petit
        else :# si x est impaire, x sera blanc
            begin_fill()
            fillcolor("white")
            down()
            circle(rc,360)
            up()
            end_fill()
            x=x+1#on ajoute 1 a x a chaque répétition
            rc=rc-(r/n)#on refix rc pour que les cercles soit de plus en plus petit
    #repositionement de la turtle au centre du cercle
    left(90)
    forward(r)
    right(90)

def perleD(r,rcouleur):
    down()
    circle(r,360)#je fais le cercle extérieur
   #tracage du contenu
    up()
    left(90)
    forward(r+r/3)# je remonte d'un rayon et 1 tier
    left(90)
    down()
    begin_fill()#je colore la perle
    fillcolor((rcouleur))
    circle(r/2,360)# je crée la tete de mickey en faisant un cercle d'un demi rayon
    end_fill()
    #tracage de la deuixème oreille
    up()
    circle(r/2,45)#je me deplace d'un quart de cercle pour tracer la première oreille
    right(90)
    backward(r/8)
    right(90)
    down()
    begin_fill()
    fillcolor((rcouleur))
    circle(r/3.5,360)#le cercle des oreilles a un rayon de rayon divisé par 3,5
    end_fill()
    #je me replace en haut de la tête de Mickey
    up()
    circle(r/3.5,-360)# je refais le cercle de l'oreille a l'envers pour ce replacer
    right(-90)
    forward(r/8)
    right(-90)
    circle(r/2,-45)
    circle(r/2,315)
    right(90)
    backward(r/8)
    right(90)
    #tracage de la deuxième oreille de Mickey
    down()
    begin_fill()
    fillcolor((rcouleur))
    circle(r/3.5,360)#le cercle des oreilles a un rayon de rayon divisé par 3,5
    end_fill()
    #je me replace en haut de la tête de Mickey
    up()
    circle(r/3.5,-360)
    right(-90)
    forward(r/8)
    right(-90)
    circle(r/2,-315)
    #placement de la turtle pour faire le premier oeuille
    left(90)
    forward(r/2)
    #premier oeille de Mickey
    begin_fill()
    fillcolor("white")
    right(90)
    forward(r/8)
    down()
    right(90)
    forward(r/16)
    circle(r/16,180)
    forward(r/8)
    circle(r/16,180)
    forward(r/16)
    end_fill()
    #repositionnement de la turtle au milieu de la tete de Mickey
    up()
    forward(-r/16)
    circle(r/16,-180)
    forward(-r/8)
    circle(r/16,-180)
    forward(-r/16)
    right(90)
    #placement pour faire le deuxième oeille de Mickey
    forward(r/4)
    #tracage du deuxième oeille de Mickey
    begin_fill()
    fillcolor("white")
    down()
    right(90)
    forward(r/16)
    circle(r/16,180)
    forward(r/8)
    circle(r/16,180)
    forward(r/16)
    end_fill()
    #repositionnement de la turtle pour continuer le collier
    up()
    right(90)
    forward(r/8)
    right(90)
    forward(r+(r/6))
    right(90)




def collier():
    np=0 #nombre de perles par collier
    pc=0 #perle choisie
    #positionnement de la turtle pour tracé le collier
    up()
    circle(250,90)
    #tracage du carré au bout du collier
    down()
    forward(15)
    left(90)
    forward(15)
    left(90)
    forward(15)
    left(90)
    forward(15)
    left(90)
    down()
    #tirage du nombre de perle
    np=randint(2,8)#np est le nombre de perle et est tiré au hasard entre 2 et 8
    #tirage au sort de la couleur des perles
    coul=(random(),random(),random())#ici la couleur est defini par 3 nombres tiré au hasard par la fonction random
    #tracage du collier
    for i in range(np): #la boucle trace une perle np-1 fois
            #mise a zero du choix de la perle
            down()
            pc=0#le choix de la perle est remis a 0 chaque tour de boucle
            circle(250,-180/(np+1))#bout de cercle tracé avant chaque perle.le degré du cercle est egale a -180 divisé par le nombre de perles
            left(180)
            #tirage de la perle
            pc=randint(1,4)#la perle est choisi aléatoirement entre les 4 perles
            if pc==1:#1 represente la perle A
                up()
                circle(200/np,180)#demi cercle non tracé de meme rayon que la perle car mes perles commence par le bas
                down()
                perleA(200/np,coul)#la perle A a pour rayon 200 divisé par le nombre de perles et couleur commune a toute les perles
            elif pc==2:#2 represente la perle B
                up()
                circle(200/np,180)#demi cercle non tracé de meme rayon que la perle car mes perles commence par le bas
                down()
                perleB(200/np,coul)#la perle B a pour rayon 200 divisé par le nombre de perles et couleur commune a toute les perles
            elif pc==3:#3 represente la perle C
                up()
                circle(200/np,180)#demi cercle non tracé de meme rayon que la perle car mes perles commence par le bas
                down()
                perleC(200/np,coul,randint(3,8))#la perle C a pour rayon 200 divisé par le nombre de perles et couleur commune a toute les perles et un nombre de perle aléatoire entre  3 et 8
            elif pc==4:#4 represente la perle D
                up()
                circle(200/np,180)#demi cercle non tracé de meme rayon que la perle car mes perles commence par le bas
                down()
                perleD(200/np,coul)#la perle D a pour rayon 200 divisé par le nombre de perles et couleur commune a toute les perles
    #tracage du deuxième carré
    down()
    circle(250,-180/(np+1))#on retrace le bout de cercle tracé avant chaque perle.le degré du cercle est egale a -180 divisé par le nombre de perles
    right(180)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    forward(15)
    #position au centre du colier pour pouvoir mettre la signature
    up()
    left(180)
    forward(250+60)#je me deplace vers la droite de la moitier de la longueur de la signature pour qu'elle soit centré
    right(90)
    forward(200/2-80)
    right(90)
    forward(175)
    right(180)
    signature()


collier()




