# Prédiction du type d'un Pokémon

## Objectifs

L'objectif de ce projet personnel est de concevoir un modèle d'intelligence artificielle capable de prédire le type d'un Pokémon à partir de ses caractéristiques intrinsèques (statistiques d'attaque, défense, etc., poids, taille, rareté...)

Compétences mobilisées :
* Extraction de données (API → JSON → CSV / Pandas)
* Analyse et visualisation de données (Power BI)
* Machine Learning (Scikit-Learn), modèles de classification (random forest, régression logistique)
* Interface Streamlit

---
## Réflexion préalable

Pour réaliser ce projet de Machine Learning, j'ai commencé par définir un objectif **réalisable** (il existe des données exploitables) et **pertinent** (l'objectif de la prédiction justifie réellement l'usage de l'intelligence artificielle).

J'ai également réfléchi à la manière d'extraire les données depuis la [PokéAPI](https://pokeapi.co/), ainsi qu'aux **données pertinentes** pour mon projet.

---
## Extraction de données

J'ai récupéré les données brutes en JSON pour chaque Pokémon, à deux endpoints :
- /pokemon/{id}
- /pokemopn-species/{id}

---
## Évolution du projet

Le projet est en cours, ce fichier évoluera à mesure de ma progression.

__Étape en cours :__ conversion des données brutes JSON en CSV exploitables avec Power BI et Pandas

Étapes terminées :
* réflexion sur la pertinence et la faisabilité du projet
* extraction des données brutes depuis la PokéAPI (endpoits /pokemon et /pokemon-species)