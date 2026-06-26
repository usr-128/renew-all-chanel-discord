# Renew All Discord Channels

Bot Discord permettant de renouveler automatiquement tous les salons d'un serveur tout en conservant leur configuration (catégories, permissions, positions, etc.).

---

## Fonctionnalités

* Renouvellement des salons textuels.
* Renouvellement des salons vocaux.
* Conservation des catégories.
* Conservation des permissions.
* Conservation de l'ordre des salons.
* Exécution rapide.
* Compatible avec les versions récentes de `discord.py`.

---

## Installation

Clonez le dépôt :

```bash
git clone https://github.com/usr-128/renew-all-chanel-discord.git
```

Accédez au dossier du projet :

```bash
cd renew-all-chanel-discord
```

Installez les dépendances :

```bash
pip install -r requirements.txt
```

---

## Configuration

Ajoutez le token de votre bot dans votre fichier de configuration.

Exemple :

```python
TOKEN = "VOTRE_TOKEN_ICI"
```

Ne partagez jamais votre token Discord.

---

## Lancement

Exécutez le fichier principal :

```bash
python main.py
```

Remplacez `main.py` par le nom du fichier principal de votre projet si nécessaire.

---

## Permissions requises

Le bot doit posséder les permissions suivantes :

* Gérer les salons
* Voir les salons
* Envoyer des messages
* Lire l'historique des messages

---

## Utilisation

Lancez la commande prévue par le bot pour renouveler l'ensemble des salons du serveur.

Le processus est le suivant :

1. Création d'une copie du salon.
2. Copie des permissions et des paramètres.
3. Remise du nouveau salon à la même position.
4. Suppression de l'ancien salon.

---

## Structure du projet

```text
renew-all-chanel-discord/
├── main.py
├── requirements.txt
├── README.md
└── ...
```

---

## Technologies utilisées

* Python 3.10 ou supérieur
* discord.py

---

## Contribution

Les contributions sont les bienvenues.

1. Forkez le projet.
2. Créez une branche pour vos modifications.
3. Effectuez vos changements.
4. Ouvrez une Pull Request.

---

## Licence

Ce projet est distribué librement. Vous pouvez le modifier et l'utiliser selon vos besoins.

---

## Auteur

Développé par **usr-128**.

Si ce projet vous est utile, vous pouvez laisser une étoile sur le dépôt GitHub.
