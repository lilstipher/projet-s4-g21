# Openface of project-21
La méthode Open Face est une méthode de reconnaissance faciale open source développée par Brandon Amos Bartosz Ludwiczuk, et Mahadev Satyanarayanan. Elle est basée sur le document FaceNet de CVR 2015 :*A Unifed Embedding for Face Recogniton and Clustering publié par les 3 ingénieurs de google Florian Schrof, Dmitry Kalenichenko, and James Philbin*. La méthode est implémentée en Python et Torch don peut être implémentée sur CPU ou GPU.

Ceci est un guide pour vous aider à utiliser `Openface` sur votre propre ordinateur.
 

## Environnement

Les instructions suivantes sont pour `Linux` et`OSX` seulement.

* Nous vous recommandons fortement d'utiliser le conteneur `Docker` sauf si vous êtes expérimenté dans la création de logiciels Linux à partir de sources.
* Dans OSX, vous devrez peut-être changer les hashbangs de `python2` à`python`.
* `OpenFace` a été testé sur `Ubuntu` 14.04 et `OSX` 10.10 et peut ne pas fonctionner correctement sur d'autres distributions.
Plus d'informations concernant l'installation sur [le site de open face](https://cmusatyalab.github.io/openface/setup/).


## Docker automatisé

Le moyen le plus rapide de commencer est d'utiliser notre build Docker automatisé préconstruit, disponible sur [bamos / openface](https://hub.docker.com/r/bamos/openface/). Cela ne nécessite pas ou n'utilise pas une copie locale d'OpenFace. Pour utiliser sur vos images, partagez un répertoire entre votre hôte et le conteneur Docker.

* Ici `local_directory` est le répertoire qui est en dehors de`Docker container`, où vous devriez placer vos images de traing. (Par exemple: / User / training-images)
* Et `remote_directory` est le répertoire qui se trouve dans`Docker container` qui a le même contenu que `local_directory`
```bash
$ docker pull bamos/openface
$ docker run -p 9000:9000 -p 8000:8000 -v /local_directory:/remote_directory -t -i bamos/openface /bin/bash
```

## Création d'un modèle de classification

### 1. Créez un répertoire d'images brutes.
Préparer `30` images, ils doivent être`2` personnes différentes, la taille de l'image n'a pas d'importance, mais il est préférable d'inclure seulement des visages, `15` images pour chaque personne, respectivement placés dans deux répertoires différents.

```bash
$ ./local_directory/traing-images
```
``` 
Structure:

personne-1
├── image image-1.jpg
├── image image-2.png
...
└── image image-15.png

personne-2
├── image image-1.png
├── image image-2.jpg
...
└── image image-15.png
```

### 2. Détection de visage

Démarrer la détection automatique

```bash
$ /root/openface/util/align-dlib.py ./training-images align outerEyesAndNose ./aligned-images/ --size 96
```


Le but de cette étape est de permettre à la machine de découper automatiquement ces 30 photos en fichiers png `96x96` pour un traitement ultérieur.

Le résultat du traitement est placé dans le répertoire `aligned-images`. Il y a deux dossiers en dessous, c'est-à-dire les noms des deux personnes que vous avez placées, et ces deux dossiers incluent les visages des deux personnes.

### 3. Générer des représentations

```bash
$ /root/openface/batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/
```

Il produit le modèle de classification qui est un SVM enregistré sur le disque en tant que pickle Python. Cette étape va générer 2 fichiers csv dans le répertoire `generated-embeddings`. Les labels `labels.csv` et `reps.csv`,`labels.csv` sont relativement simples, ils montrent juste quelle photo correspond à quelle personne, et `reps.csv` est un grand nombre de matrices.

### 4. Créez le mode de classification

```bash
$ /root/openface/demos/classifier.py train ./generated-embeddings
```

Le résultat de l'apprentissage générera un fichier `classifier.pkl` dans le répertoire`generated-embeddings`. C'est ce que nous voulons finalement.

## Reconnaissance de visage
Vous pouvez maintenant commencer à tester et copier une image dans `/ local_directory` qui ne se trouve pas dans l'ensemble de données. Cette photo peut inclure le fond ou le corps entier, mais il est préférable de ne pas mettre une photo de plusieurs personnes, ou la machine ne sait pas laquelle vous voulez identifier.

En supposant que le fichier photo est `local_directory / 1.jpg`

```bash
$ /root/openface/demos/classifier.py infer ./generated-embeddings/classifier.pkl 1.jpg
```


Si la personne sur la photo est l'une des deux personnes identifiées tout à l'heure, la précision de la reconnaissance sera supérieure à 90%. Sinon, ce sera moins de 80%.

## En plus
Lien du docker utilisé pour le projet 21 disponible [ici](https://hub.docker.com/r/haipengli/projet_21_openface/)