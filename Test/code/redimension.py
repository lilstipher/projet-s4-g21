# Objectif : redimensionner en masse des images dans un dossier, avant utilisation pour blog ou partage par email par exemple
# TODO : fix si fichier non image présent dans le dossier (genre .directory), fait mais hard codé sur terminaison fichier image en "G" ou "g"

from PIL import Image
from os import listdir
from os.path import isfile, join

mypath ="/home/hmkouassi/Bureau/S4/projet-s4-g21/Test/code/img"
redimpath ="/home/hmkouassi/Bureau/S4/projet-s4-g21/Test/code/img/redim"
imageFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
#target = int(input("Dimension maximum voulue (ex 1000) : "))
redimRatio=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

for im in imageFiles :
    im1 = Image.open(join(mypath,im))
    originalWidth, originalHeight = im1.size
    for i in redimRatio :
        width = int(originalWidth*i)
        height = int(originalHeight*i)
        im2 = im1.resize((width, height), Image.ANTIALIAS) # linear interpolation in a 2x2 environment
        im2.save(join(redimpath, "".join([str(width),"x",str(height),"_",im])))
    #print (im, "redimensionnée…")
print ("Travail terminé !", len(imageFiles), "images redimensionnées.")