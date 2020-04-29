# Docker - Cheat sheet

#### Définition de Docker :
Docker permet d'embarquer une application dans un ou plusieurs containers logiciels qui pourra s'exécuter sur n'importe quel serveur machine, qu'il soit physique ou virtuel.

Visiter [docker](https://www.docker.com/) pour en savoir plus

## Commande de base

Toutes les commandes docker commence par : `docker`

### Manipulation des containers

```bash
docker container # Base

docker container run --name 'Nom du container' -p 'Port' # Lancer un container
docker container stop 'Nom du container' # Stopper un container
docker container ls  # Affiche la liste des containers
docker container create 'Options' 'Image' # Créer un container
docker container rm 'ID du container' # Supprimer un container
```

### Manipulation des images

```bash
docker image # Base

docker image build # Construire une image
docker image pull # Récupérer une image située dans un repository du docker hub
docker image push # Publier une image dans un repository du docker hub
docker image ls  # Affiche la liste des images
docker image save # Sauvegarder une image
docker image rm 'ID de l'image' # Supprimer une image
```

## Docker Hub
Docker Hub est un service fourni par Docker pour trouver et partager des images de conteneurs avec votre équipe.

Rendez-vous sur [docker hub](https://hub.docker.com/) pour en savoir plus.

## Documentation supplémentaire
Pour plus d'informations sur docker, les commandes, etc.

Voir la [documentation](https://docs.docker.com/).
