# Cybersecurity Python Labs

## Vue d'ensemble

Ce dépôt contient de petits labs pédagogiques Python sur les fondamentaux de la cybersécurité. Utilisez-les uniquement dans des environnements locaux, des réseaux isolés, des systèmes qui vous appartiennent ou des scénarios explicitement autorisés.

Les scripts sont des exercices d'apprentissage, pas des outils approuvés pour des opérations offensives réelles.

## Cadre éthique

- Obtenez une autorisation avant tout test.
- Préférez `localhost`, `127.0.0.1` et les réseaux de laboratoire isolés.
- Utilisez des valeurs réservées à la documentation comme `192.0.2.1`.
- N'utilisez pas d'identifiants, numéros de téléphone, URLs, fichiers ou données personnelles réels.
- Ne publiez pas de résultats de scan ou d'informations concernant des tiers.

## Domaines étudiés

Le dépôt contient des labs locaux sur les hashes, la génération de mots de passe, les permutations de texte, les sockets, le scan de ports, le ping, les calculs IP, le parsing web, la stéganographie et les métadonnées.

Les labs réseau, web et métadonnées nécessitent une autorisation explicite.

## Installation

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Placeholders sûrs

- `localhost`
- `127.0.0.1`
- `192.0.2.1`
- `https://example.com/`
- `LAB_PLACEHOLDER_MESSAGE`

## Limites

- Certains scripts sont des études initiales ou incomplètes.
- Les labs réseau génèrent du trafic et doivent rester dans des environnements autorisés.
- Les services externes peuvent collecter des métadonnées.
- Ce dépôt ne fournit pas d'instructions pour viser des cibles réelles.

Voir [SECURITY.md](../../SECURITY.md) et [SECURITY_NOTES.md](../../SECURITY_NOTES.md).
