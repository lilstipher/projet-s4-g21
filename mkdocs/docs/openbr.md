# Open Br
OpenBr est un projet open-source qui vise à améliorer les algorithmes existants, de s'interfacer avec des systèmes commerciaux, de mesurer les performances de reconnaissance et de déployer des systèmes biométriques automatisés. Le projet est conçu pour faciliter le prototypage rapide d'algorithmes, et dispose d'un cadre de base mature, d'un système de plug-in flexible et d'un support pour le développement de sources ouvertes et fermées. Des algorithmes prêts à l'emploi sont également disponibles pour des modalités spécifiques, notamment la reconnaissance faciale, l’estimation de l'âge et l'estimation du genre. Les créateurs sont J. Klontz, B. Klare, S. Klum, M. Burge, A. Jain.
## installation 
OpenBR est pris en charge sur plusieurs systèmes d'exploitation.
Notamment:

* Linux
* Mac Os X
* Windows

Cepedant nous avons préparé une `machine virtuelle linux` déjà prête à l'emploi. [Disponible ici](www.linktoadd.com).

### Installation Linux

1. Installer GCC 4.9.2

        $ sudo apt-get update
        $ sudo apt-get install build-essential

2. Installer CMake 3.0.2

        $ sudo apt-get install cmake cmake-curses-gui

3. [Télécharger OpenCV 2.4.11](http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.11/opencv-2.4.11.zip/download), **Aussi** [Faire un build OpenCV avec support vidéo](https://github.com/biometrics/openbr/wiki/Build-OpenCV-with-Video-Support-on-Ubuntu)

        $ cd ~/Downloads
        $ unzip opencv-2.4.11.zip
        $ cd opencv-2.4.11
        $ mkdir build
        $ cd build
        $ cmake -DCMAKE_BUILD_TYPE=Release ..
        $ make -j4
        $ sudo make install
        $ cd ../..
        $ rm -rf opencv-2.4.11*


4. Installer Qt 5.4.1

        $ sudo apt-get install qt5-default libqt5svg5-dev qtcreator

5. Avec un compte [GitHub](https://github.com/) 

        $ git clone https://github.com/biometrics/openbr.git
        $ cd openbr
        $ git checkout v1.1.0
        $ git submodule init
        $ git submodule update

6. Build OpenBR!

        $ mkdir build # from the OpenBR root directory
        $ cd build
        $ cmake -DCMAKE_BUILD_TYPE=Release ..
        $ make -j4
        $ sudo make install

7. Hack OpenBR!
    1. Open Qt Creator IDE

        $ qtcreator &

    2. From the Qt Creator "File" menu select "Open File or Project...".
    3. Select "openbr/CMakeLists.txt" then "Open".
    4. Browse to your pre-existing build directory "openbr/build" then select "Next".
    5. Select "Run CMake" then "Finish".
    6. You're all set! You can find more information on Qt Creator [here](http://qt-project.org/doc/qtcreator) if you need it.

8. (Optionel) Tester OpenBR (un peu lourd)!

        $ cd openbr/scripts
        $ ./downloadDatasets.sh
        $ cd ../build
        $ make test

9. (Optionel) Package OpenBR!

        $ cd openbr/build
        $ sudo cpack -G TGZ

10. (Optionel) Build OpenBR documentation!
    1. Générer la documentation

            $ pip install mkdocs
            $ cd openbr/docs
            $ sh build_docs.sh
            $ mkdocs serve

    2. Taper `http://127.0.0.1:8000` dans votre ordinateur pour voir la docs.

---

### OSX

1.Téléchargez et installez les derniers outils «XCode» et «Command Line Tools» sur [la page Téléchargements de développeurs Apple].(https://developer.apple.com/downloads/index.action#) page.

2. [Télécharger CMake 3.0.2](http://www.cmake.org/files/v3.0/cmake-3.0.2.tar.gz)

            $ cd ~/Downloads
            $ tar -xf cmake-3.0.2.tar.gz
            $ cd cmake-3.0.2
            $ ./configure
            $ make -j4
            $ sudo make install
            $ cd ..
            $ rm -rf cmake-3.0.2*

3. [Télécharger OpenCV 2.4.11](http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.11/opencv-2.4.11.zip/download)

        $ cd ~/Downloads
        $ unzip opencv-2.4.11.zip
        $ cd opencv-2.4.11
        $ mkdir build
        $ cd build
        $ cmake -DCMAKE_BUILD_TYPE=Release ..
        $ make -j4
        $ sudo make install
        $ cd ../..
        $ rm -rf opencv-2.4.11*

4. [Télécharger et installler Qt 5.4.1](http://download.qt.io/official_releases/qt/5.4/5.4.1/qt-opensource-mac-x64-clang-5.4.1.dmg)

5. Avec un compte [GitHub](https://github.com/)

        $ git clone https://github.com/biometrics/openbr.git
        $ cd openbr
        $ git checkout v1.1.0
        $ git submodule init
        $ git submodule update

6. Build OpenBR!

        $ mkdir build # from the OpenBR root directory
        $ cd build
        $ cmake -DCMAKE_PREFIX_PATH=~/Qt/5.4.1/clang_64 -DCMAKE_BUILD_TYPE=Release ..
        $ make -j4
        $ sudo make install

7. Hack OpenBR!
    1. Open Qt Creator IDE

            $ open ~/Qt/Qt\ Creator.app

    2. From the Qt Creator "File" menu select "Open File or Project...".
    3. Select "openbr/CMakeLists.txt" then "Open".
    4. Browse to your pre-existing build directory "openbr/build" then select "Continue".
    5. Select "Run CMake" then "Done".
    6. You're all set! You can find more information on Qt Creator [here](http://qt-project.org/doc/qtcreator) if you need it.

8. (Optionel) Tester OpenBR (un peu lourd)!

        $ cd openbr/scripts
        $ ./downloadDatasets.sh
        $ cd ../build
        $ make test


9. (Optional) Package OpenBR!

        $ cd openbr/build
        $ sudo cpack -G TGZ


10. (Optional) Build OpenBR documentation!
    1. Générer la doc

            $ pip install mkdocs
            $ cd openbr/docs
            $ sh build_docs.sh
            $ mkdocs serve

    2. Taper `http://127.0.0.1:8000` dans votre ordinateur pour voir la docs.

---

### Windows
1. [Téléchargez Visual Studio Express 2013 pour Windows Desktop](http://go.microsoft.com/?linkid=9832280&clcid=0x409) et installez-le. Vous devrez vous enregistrer auprès de Microsoft, mais c'est gratuit.e.

2. [Télécharger et installer CMake 3.0.2](http://www.cmake.org/files/v3.0/cmake-3.0.2-win32-x86.exe)
     1. Pendant la configuration de l'installation, sélectionnez "Ajouter CMake à PATH".

3. [Télécharger OpenCV 2.4.11](https://github.com/Itseez/opencv/archive/2.4.11.zip)
     1. Considérez le programme open source gratuit [7-Zip](http://www.7-zip.org/) si vous avez besoin d'un programme pour désarchiver les archives.
     2. Déplacez le dossier "opencv-2.4.11" sur "C: \".
     3. Ouvrir  "l'invite de commande VS2013 x64 Cross Tools "  (dans le menu Démarrer, sélectionnez «Tous les programmes» -> «Microsoft Visual Studio 2013» -> «Outils Visual Studio» -> «Invite de commandes VS2013 x64 Cross Tools») :
            $ cd C:\opencv-2.4.11
            $ mkdir build-msvc2013
            $ cd build-msvc2013
            $ cmake -G "NMake Makefiles" -DBUILD_PERF_TESTS=OFF -DBUILD_TESTS=OFF -DWITH_CUDA=OFF -DWITH_FFMPEG=OFF -DCMAKE_BUILD_TYPE=Debug ..
            $ nmake
            $ nmake install
            $ cmake -DCMAKE_BUILD_TYPE=Release ..
            $ nmake
            $ nmake install
            $ nmake clean

4. [Télécharger et Installer Qt 5.4.1](http://download.qt.io/official_releases/qt/5.4/5.4.1/qt-opensource-windows-x86-msvc2013_64-5.4.1.exe)

5. Avec un compte [GitHub](https://github.com/) 

            $ cd /c
            $ git clone https://github.com/biometrics/openbr.git
            $ cd openbr
            $ git checkout v1.1.0
            $ git submodule init
            $ git submodule update

6. Build OpenBR!
    1. From the VS2013 x64 Cross Tools Command Prompt:

            $ cd C:\openbr
            $ mkdir build-msvc2013
            $ cd build-msvc2013
            $ cmake -G "CodeBlocks - NMake Makefiles" -DCMAKE_PREFIX_PATH="C:/opencv-2.4.11/build/install;C:/Qt/Qt5.4.1/5.4/msvc2013_64" -DCMAKE_INSTALL_PREFIX="./install" -DBR_INSTALL_DEPENDENCIES=ON -DCMAKE_BUILD_TYPE=Release ..
            $ nmake
            $ nmake install

   2. Découvrez le dossier "install".

7. Hack OpenBR!
    1. From the VS2013 x64 Cross Tools Command Prompt:
        $ C:\Qt\Qt5.4.1\Tools\QtCreator\bin\qtcreator.exe
    2. From the Qt Creator "Tools" menu select "Options..."
    3. Under "Kits" select "Desktop (default)"
    4. For "Compiler:" select "Microsoft Visual C++ Compiler 11.0 (x86_amd64)" and click "OK"
    5. From the Qt Creator "File" menu select "Open File or Project...".
    6. Select "C:\openbr\CMakeLists.txt" then "Open".
    7. If prompted for the location of CMake, enter "C:\Program Files (x86)\CMake 3.0.2\bin\cmake.exe".
    8. Browse to your pre-existing build directory "C:\openbr\build-msvc2013" then select "Next".
    9. Select "Run CMake" then "Finish".
    10. You're all set! You can find more information on Qt Creator <a href="http://qt-project.org/doc/qtcreator">here</a> if you need.

8. (Optional) Package OpenBR!
    1. From the VS2013 x64 Cross Tools Command Prompt:
        $ cd C:\openbr\build-msvc2013
        $ cpack -G ZIP

---

### Face Recognition

Ce tutoriel donne un exemple sur la façon d'effectuer une reconnaissance de visage dans OpenBR. OpenBR implémente l'algorithme 4SF [^2](http://openbiometrics.org/docs/tutorials/#fn:2) pour effectuer la reconnaissance faciale. Veuillez lire le "paper" pour plus de détails sur l'algorithme. 


Pour commencer, On peut faire la reconnaissance faciale à partir de l'invite de commande. Ouvrez le terminal et entrez:

    $ br -algorithm FaceRecognition \
        -compare ../data/MEDS/img/S354-01-t10_01.jpg ../data/MEDS/img/S354-02-t10_01.jpg \
         -compare ../data/MEDS/img/S354-01-t10_01.jpg ../data/MEDS/img/S386-04-t10_01.jpg

Assez facile? Vous devriez voir les résultats sur le terminal qui ressemblent à :

    $ Set algorithm to FaceRecognition
    $ Loading /usr/local/share/openbr/models/algorithms/FaceRecognition
    $ Loading /usr/local/share/openbr/models/transforms//FaceRecognitionExtraction
    $ Loading /usr/local/share/openbr/models/transforms//FaceRecognitionEmbedding
    $ Loading /usr/local/share/openbr/models/transforms//FaceRecognitionQuantization
    $ Comparing ../data/MEDS/img/S354-01-t10_01.jpg and ../data/MEDS/img/S354-02-t10_01.jpg
    $ Enrolling ../data/MEDS/img/S354-01-t10_01.jpg to S354-01-t10_01r7Rv4W.mem
    $ 100.00%  ELAPSED=00:00:00  REMAINING=00:00:00  COUNT=1
    $ 100.00%  ELAPSED=00:00:00  REMAINING=00:00:00  COUNT=1
    $ 1.8812
    $ Comparing ../data/MEDS/img/S354-01-t10_01.jpg and ../data/MEDS/img/S386-04-t10_01.jpg
    $ Enrolling ../data/MEDS/img/S354-01-t10_01.jpg to S354-01-t10_01r7Rv4W.mem
    $ 100.00%  ELAPSED=00:00:00  REMAINING=00:00:00  COUNT=1
    $ 100.00%  ELAPSED=00:00:00  REMAINING=00:00:00  COUNT=1
    $ 0.571219

Alors, qu'est-ce que `FaceRecognition`? C'est une abbrieviation pour simplifier l'exécution de l'algorithme. Toutes les abréviations d'algorithmes se trouvent dans ```openbr / plugins / core / algorithms.cpp```.

Il est également possible:

* Évaluer les performances de reconnaissance de faciale (Notez que cela nécessite [R](http://www.r-project.org/)):
```
        $ br -algorithm FaceRecognition -path ../data/MEDS/img/ \
        -enroll ../data/MEDS/sigset/MEDS_frontal_target.xml target.gal \
        -enroll ../data/MEDS/sigset/MEDS_frontal_query.xml query.gal \
        -compare target.gal query.gal scores.mtx \
        -makeMask ../data/MEDS/sigset/MEDS_frontal_target.xml ../data/MEDS/sigset/MEDS_frontal_query.xml MEDS.mask \
        -eval scores.mtx MEDS.mask Algorithm_Dataset/FaceRecognition_MEDS.csv \
        -plot Algorithm_Dataset/FaceRecognition_MEDS.csv MEDS
```

* Effectuez une recherche de reconnaissance faciale 1:N.

    	$ br -algorithm FaceRecognition -enrollAll -enroll ../data/MEDS/img 'meds.gal'
    	$ br -algorithm FaceRecognition -compare meds.gal ../data/MEDS/img/S001-01-t10_01.jpg match_scores.csv

* Entrainer un nouvel algorithme de reconnaissance faciale (sur une autre base):

    	$ br -algorithm 'Open+Cvt(Gray)+Cascade(FrontalFace)+ASEFEyes+Affine(128,128,0.33,0.45)+(Grid(10,10)+SIFTDescriptor(12)+ByRow)/(Blur(1.1)+Gamma(0.2)+DoG(1,2)+ContrastEq(0.1,10)+LBP(1,2)+RectRegions(8,8,6,6)+Hist(59))+PCA(0.95)+Normalize(L2)+Dup(12)+RndSubspace(0.05,1)+LDA(0.98)+Cat+PCA(0.95)+Normalize(L1)+Quantize:NegativeLogPlusOne(ByteL1)' -train ../data/ATT/img FaceRecognitionATT

L'API de ligne de commande est documentée [ici](http://openbiometrics.org/docs/api_docs/cl_api/).
