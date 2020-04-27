# TD n°1 - NoSQL M1 WEB - H3 Hitema
_______________

# Au programme 🤖

* Lundi 27 avril :
	* Rapels python et POO
	* Statistiques descriptives et datavisualisation avec numpy, pandas et seaborn 
  
* Mardi 28 avril : 
	* Statistiques descriptives avec numpy et pandas (suite)
	* Rappels shell linux & bash 
  
* Mercredi 29 avril : 
	* Workshop Docker et python  


_______________


## Pré-requis

- Connaissance de la programmation orientée objet en Python 
- Mathématique niveau bac scientifique  
- De la bonne humeur et de la motivation durant cette période de confinement 🚀



## Suivi 📈

Créer un repo github et faire a minima deux pushs par jour (matin et aprem) afin que je vois ou vous en êtes 👌


## Rappels python et POO 👨‍🎓


Python est un langage de programmation inventé par Guido van Rossum. La première version de python est sortie en 1991. Il est notamment **l'un des langages de programmation les plus intéressants du moment. 🔭**

Les mesures de *l’indice PyPL* du mois de mai 2018 se caractérisent par l’arrivée de Python, pour la première fois, à la tête du classement des langages de programmation les plus populaires selon le baromètre. L'indice PyPL évalue la popularité des langues en fonction de la fréquence de recherche dans les didacticiels du langage. 
<https://www.developpez.com>


Facile à apprendre, python est souvent utilisé en exemple lors de l'apprentissage de la programmation. Avec les variables, les boucles et les fonctions, on connaît suffisamment d’éléments pour écrire des programmes simples. 

**Python est à la fois simple et puissant**, il vous permet d'écrire des scripts très simples mais grâce à ses nombreuses bibliothèques, vous pouvez travailler sur des projets plus ambitieux.

Il est parfois **jusqu'à 5 fois plus concis que le langage Java ⚡️** par exemple, ce qui augmente la productivité du développeur et réduit mécaniquement le nombre de bugs. L'environnement python est notamment très riche en librairies. Vous trouverez toujours des projets open source qui vous faciliteront la vie notamment sur <https://github.com/>.

Vérifions que python est bien installé sur votre machine.  

#### Emplacement 
```
which python 
```

#### Version 
``` 
python --version 
```

où encore 
```
python -V 
```


#### Le gestionnaire de paquets python `pip`
Un gestionnaire de paquet est un (ou plusieurs) outil(s) automatisant le processus d'installation, désinstallation, mise à jour de logiciels installés sur un système informatique. Dans notre cas il s'appelle `pip` vous pouvez l'installer en suivant la documentation officielle [ici](https://pip.pypa.io/en/stable/installing/) 🤓


Vous pouvez vérifier que `pip` est bien installé avec la commande suivante : 

``` 
pip --version   
```

Vous pouvez aussi voir les paquets/librairies installés via `pip` avec : 

``` 
pip list   
```

Plus généralement vous pouvez avoir plus de détail avec l'option `help` et : 
```
pip --help
```

#### Travailler avec jupyter notebook 

Jupyter est une application web utilisée pour programmer dans plus de 40 langages de programmation, dont Python, Julia, Ruby, R, ou encore Scala. 


### Travailler avec jupyter sur votre machine 

De façon technique Jupyter est un IDE sous forme de serveur web. Vous pouvez donc lancer un serveur Jupyter depuis votre machine via le `localhost` ou bien passer par le web avec l'outil de google que nous verrons dans la suite de ce cours. 


#### Installation
Ouvrez un terminal et taper la commande suivante : 
```bash
pip install jupyter
```

#### Running Jupyter
Maintenant que jupyter est installé vous pouvez travailler dans un `notebook`. Pour cela, positionnez vous dans votre dossier de travail et lancer la commande :
```bash
jupyter notebook 
```

#### Qu'est-ce qu'un fichier ipynb?

Il est utile de comprendre ce qu'est un fichier `.ipynb`.
Ce sont des fichiers texte qui décrivent le contenu de votre `notebook` dans un format appelé `JSON`. 

Chaque *cellule* et son contenu, y compris les pièces jointes ont été converties en chaînes de texte, y sont répertoriés avec certaines métadonnées. C'est pour cela que si vous ouvrez un fichier `.ipynb` sans la commande `jupyter notebook` vous verez ceci : 


#### Le Markdown 

Markdown est un langage de balisage léger et facile à apprendre pour formater du texte brut. Sa syntaxe a une correspondance avec les balises HTML, donc certaines connaissances préalables ici seraient utiles mais ne sont certainement pas une condition préalable.

Rappelez-vous que cet article a été écrit dans un cahier Jupyter, donc tout ce que vous avez vus jusqu'à présent a été réalisés en Markdown. On peut couvrir les bases rapidement en quelques lignes. 


```
# Ceci est un titre de niveau 1
## Ceci est un titre de niveau 2
### Ceci est un titre de niveau 3

Tout simplement un paragraphe. 

Ajoutez du texte en gras via **mon texte en gras** et en italic avec *mon texte en italic*

Les paragraphes doivent être séparés par un retour à la ligne.

Pour inclure une liste il faut utiliser * : 
* un item
* un autre item 
    * un sous item 

1. Les listes peuvent également être numérotées.
2. comme cela 

[Il est possible d'inclure des hyperliens](https://www.example.com)

On peut ajouter du code avec les ` tel que : `foo()`
On peut aussi ajouter du code en mode 'block' avec 3 ` pour encapsuler le code. 

```


#### Jupyter dans le cloud google avec [Google colab](http://colab.research.google.com/)

Vous pouvez suivre ce cours avec l'outil [colab](http://colab.research.google.com/) de Google qui vous donne accès à des notebook dans le cloud.

Par ailleurs, ils ont une très bonne vidéo d'introduction 🤔

Avec le Drive Google vous pouvez enregistrer vos fichier notebook dans le cloud et les ouvrir avec `colab` comme application par défaut. 

Vous pouvez par exemple faire une copie de ce notebook dans votre drive et l'ouvrir avec colab afin de travailler dessus. L'avantage est que beaucoup de librairies sont déjà installées 🤓 




### Vos missions 
* installer votre environement de travail 
	* installer python sur votre machine (si vous ne l'avez pas)
	* installer jupyter sur votre machine, ouvrez le fichier `ObjetPython.ipynb`
* faire les exercices à la fin du fichier. Le fichier est situé dans le dossier python du drive [ici](https://drive.google.com/drive/folders/1ztAIyKbwjLUnLlOvQ0YidpNwXIhDAF8o?usp=sharing)


## Statistiques descriptives et datavisualisation avec numpy, pandas et seaborn 📊






#### Seaborn 
La librairie python [seaborn](https://www.google.com/search?client=safari&rls=en&q=seaborn&ie=UTF-8&oe=UTF-8) permet d'intégrer dans vos graphiques les objets `pandas.DataFrame` ce qui est assez pratique 🔌




### Vos missions 

* prendre en main les librairies numpy, pandas et seaborn  
* expliquer ce que sont : une statistique, un echantillon et un écart type.  
* se renseigner sur les objets `pandas.Series` et `pandas.DataFrame`, en quoi sont ils plus pratique que les types de bases de python ? 
* faire la feuille d'exercices dans dossier dataviz (les data sont sur le dossier data du drive) [ici](https://drive.google.com/drive/folders/1ztAIyKbwjLUnLlOvQ0YidpNwXIhDAF8o?usp=sharing)


## Rappels shell linux & bash  🛰


Parce que linux c'est gratuit, linux c'est la vie papy 👾




### Vos missions 

- Créer un script `sum.sh` qui prend 2 variables a(=20) et b(=30) et affiche une varibale  sum=a+b
- Créer un script `nameUser.sh ` qui afficher le nom de l'utilisateur ainsi que la date du jour. Le script devra demander le nom à l'utilisateur et qui l'écrit dans la console
- Créer un script `compt.sh ` qui affiche une variable count (compteur) qui s'incrémente et s'arrète au chiffre 5
- Créer un script `for.sh` qui affiche les chiffre de 10 à 1 sur une ligne à l'aide d'une boucle for
- Créer un script `if.sh` qui demande un nombre à l'utilisateur et indique si c'est un nombre à 1, 2 ou 3 chiffres
- Créer un script `cmd.sh` qui demande deux arguments (X et Y)  à l'utilisateur, qui les lis et affiche la somme dans l'interface de commande
- Créer un dossier test et un script `dir.sh` qui affiche les dossiers dans le repertoire
- Créer un nouveau fichier txt (non vide) et créer un script `lines.sh` qui itère dans votre répertoire et affiche seulement les fichiers et compte le nombre de lignes et de mots de chacun des fichiers. Afficher seulement les fichier non vides


## Workshop Docker et python 🐳


Docker est un logiciel libre permettant de lancer des applications dans des conteneurs logiciels.
Il ne s'agit pas de virtualisation, mais de conteneurisation, une forme plus légère qui s'appuie sur certaines parties de la machine hôte pour son fonctionnement. Cette approche permet d'accroître la flexibilité et la portabilité d’exécution d'une application, laquelle va pouvoir tourner de façon fiable et prévisible sur une grande variété de machines hôtes, que ce soit sur la machine locale, un cloud privé ou public, etc. Plus d'information sur la documentation officielle [ici](https://docs.docker.com/v17.09/). 

Docker a été inventé pour résoudre un probleme classique que nous avons tous rencontré en informatique. 
Un meme parle toujours mieux que milles mots : 
<div style="text-align:center">
<img src="https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd">
</div>


### Vos missions 


**Quickstart** 

* comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
* installer docker sur votre machine (Ubuntu de préférence) 
* lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
* regarder si votre container est bien lancer 
* faire un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers 
* vérifier en vous connectant à votre container qu'il est bien `up` et qu'il s'aggit bien 
* créer un repo github pour les deux jours  ⚠️avec un README.md explicite svp⚠️
* faire un push de votre travail sur votre repo et m'envoyer le lien. 

**DS Sand box container**

* coder un container type *data engineering sandbox* à partir d'une image Ubuntu    contenant : 
	* un espace de travail appelé workspace 
	* python3, pip3 et vim 
	* une installation automatique du fichier `requirements.txt`
	* un set up des credentials git pour l'utilisateur du container
	* une exposition du port 8000 
	* pour finir le container devra lancer jupyter notebook avec votre git clonné à la racine  
* faire un push de votre travail sur votre repo. 
* faire un résumé type *cheat sheet* des principales commandes des `Dockerfile`
* expliquer à quoi sert la commance ci-dessous 

#### Une commande qui peut vous servir   
```bash
$ sudo groupadd docker
$ sudo gpasswd -a $USER docker
```



## Les ressources utiles 👀

### Les bases en rapide
- python doctor : https://python.doctor
- cours oc complet en francais : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python
- rapide & précis (francais) : https://www.pierre-giraud.com/python-apprendre-programmer-cours/ 
- glossaire ml/ia : https://developers.google.com/machine-learning/glossary 
- Cheat sheet ml/ia : https://ml-cheatsheet.readthedocs.io/en/latest/
- cheat sheet bash : https://devhints.io/bash 

### Docker 
- doc : https://www.docker.com
- how to write a dockerfile : https://www.educative.io/edpresso/how-do-you-write-a-dockerfile | https://www.codementor.io/@aviaryan/writing-your-first-dockerfile-7e0rjhual 
- plus de détail : https://takacsmark.com/dockerfile-tutorial-by-example-dockerfile-best-practices-2018/ 
- best practice : https://engineering.bitnami.com/articles/best-practices-writing-a-dockerfile.html 
- pour aller plus loin : https://www.katacoda.com/courses/container-runtimes 