# Face Recognition

Reconnaître et manipuler les visages de Python ou de la ligne de commande avec
la bibliothèque de reconnaissance faciale la plus simple au monde.

Construit en utilisant [dlib](http://dlib.net/) la reconnaissance de visage à la fine pointe de la technologie
construit avec un apprentissage profond. Le modèle a une précision de 99,38% sur le
[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/).


## Installation

### Exigences
* Python 3.3+ ou Python 2.7
* macOS ou Linux (Windows n'est pas officiellement supporté, mais pourrait fonctionner)

### Options d'installation:

#### Installation sur Mac ou Linux

Tout d'abord, assurez-vous que dlib est déjà installé avec les dépendances Python:

```bash
pip3 installer dlib
```

Afin d'installer correctement dlib, vous devrez peut-être installer [cmake](https://cmake.org/)


Ensuite, installez ce module à partir de pypi en utilisant `pip3` (ou`pip2` pour Python 2):

```bash
pip3 installer face_recognition
```

Si vous rencontrez des problèmes avec l'installation, vous pouvez également essayer
[VM préconfigurée](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b).

#### Installation sur Raspberry Pi 2+

* [Instructions d'installation de Raspberry Pi 2+](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65)

#### Installation sous Windows

Bien que Windows ne soit pas officiellement pris en charge, il existe des méthodes pour le faire

* Guide d'installation de Windows 10 de @ masoudr [dlib + face_recognition](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508).

#### Installation d'une image de machine virtuelle préconfigurée

s* [Télécharger l'image VM préconfigurée](https://medium.com/@ageitgey/try-deep-learning-in-python-now-with-a-fully-pre-configured-vm-1d97d4c3e9b) (pour VMware Player ou VirtualBox).

## Utilisation

### L'entrainement du classificateur KNN
Afin de pouvoir reconnaître les visages, nous devons créer un classificateur et le sauvegarder à l'avance.
#### Créer un dossier d'ensemble d'apprentissage

```
Structure:
        <train_dir> /
        ├── <personne1> /
        Som ├── <nom de famille> .jpeg
        │ ├── <nomdufichier2> .jpeg
        │ ├── ...
        ├── <personne2> /
        Som ├── <nom de famille> .jpeg
        │ └── <nomdufichier2> .jpeg
        └── ...
```
#### Entrainer et enregistrer un classificateur KNN
```bash
knn_train.py --training-path --clf-saving-path
```
Où `training-path`est le dossier contenant les images d'apprentissage et`clf-saving-path` est le fichier classificateur (au format `.clf`).

### Identifier les visages en utilisant le classificateur créé
Comme le classificateur KNN est bien entrainé et enregistré, nous n'avons plus besoin de d'entrainer le classificateur chaque fois que nous utilisons le modèle. 
Cependant si on change de modèle on devra refaire l'entrainement, ie si on veut ajouter de nouvelles personnes dans la base d'apprentissage.
```bash
knn.py --clf-load-path --testing-path
```
Où clf-load-path est le fichier du classificateur et testing-path est le chemin de toute l'image de test.

Une fois la reconnaissance terminée, un fichier `result.txt` sera créé, dans lequel la première colonne est le nom reconnu et la deuxième colonne le nom réel du fichier.