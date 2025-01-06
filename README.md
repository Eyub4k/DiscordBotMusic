# Discord Music Bot

Ce projet est un bot Discord simple qui permet de jouer de la musique dans un canal vocal. Il utilise `discord.py` pour l'intégration Discord et `yt-dlp` pour extraire la musique depuis YouTube.

## Fonctionnalités

- Lecture de musique à partir de liens YouTube via la commande `!play <url>`.
- Le bot rejoint automatiquement le canal vocal de l'utilisateur pour jouer la musique.
- Commande `!leave` pour faire quitter le bot du canal vocal.

## Prérequis

Avant de lancer le bot, assure-toi d'avoir les éléments suivants installés :

- **Python 3.8+**
- **FFmpeg** : Le bot utilise FFmpeg pour traiter les fichiers audio.
- **Bibliothèques Python** :
  - `discord.py`
  - `yt-dlp`

### Installation

1. Clone ce dépôt sur ton ordinateur :

   ```bash
   git clone https://github.com/Eyub4k/DiscordBotMusic.git
   cd DiscordBotMusic
