# Dockerfile - Cheat sheet

#### Définition de Dockerfile :
Les Dockerfiles sont des fichiers qui permettent de construire une image Docker adaptée à nos besoins, étape par étape.

## Le fichier

Pour commencer, créez un nouveau fichier Dockerfile à la racine de votre projet.

```bash
nano dockerfile # Création du fichier dockerfile
```

### Commandes de base

```js
FROM 'image':'version' //Sur quel image le container va se baser

RUN 'commande' // Exécuter une commande

ADD 'fichier ou dossier' // Créer un fichier ou un dossier

WORKDIR 'dossier' // Dossier sur lequel on va se placer

CMD ou ENTRYPOINT 'commande' // Lancement d'une commande au démarrage du conteneur (ex: serveur jupyter notebook)

EXPOSE 'port' // Port(s) écouté(s) par le conteneur
```

## Explication des commandes

Les commandes ci-dessous permettent d'utiliser les conteneurs LINUX en enlevant les privilèges 'root'.
C'est utile dans le cas ou l'on déploie notre images à d'autres personnes.

```bash
$ sudo groupadd docker
$ sudo gpasswd -a $USER docker
```

## Documentation supplémentaire
Pour plus d'informations sur docker, les commandes, etc.

Voir la [documentation](https://docs.docker.com/).
