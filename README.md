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
- /pokemon-species/{id}

J'ai ensuite extrait les informations pertinentes pour chaque Pokémon et j'ai généré un fichier CSV qui servira :
- pour l'analyse de données avec Power BI
- pour la modélisation avec Pandas et Scikit-Learn.

---
## Analyse et visualisation de données

J'ai transformé l'unique table de mon fichier CSV en un modèle en étoile dans Power BI :
* une table de dimensions Pokédex avec les informations basiques (id, nom, génération, légendaire)
* une table de dimensions Types avec une association id-type par ligne
* une table de dimensions Évolutions avec la chaîne d'évolution d'un Pokémon et son niveau d'évolution
* une table de faits Statistiques (poids, taille, statistiques de combat, bonheur, taux de capture...)

L'analysé de données m'a permis d'établir des recommandations pour l'élaboration du modèle :
* équilibrer les données (certains types sont moins représentés que d'autres)
* regrouper les Pokémons légendaires, mythiques, Paradoxes et Ultra-Chimères avec une variable *is_special*
* utiliser le niveau d'évolution du Pokémon et y inclure la caractéristique *is_baby*
* se baser en priorité sur la répartition des statistiques de combat, ainsi que l'écart-type pour identifier les Pokémons ayant une statistique prédominante, ou au contraire une répartition équilibrée
* créer une variable *is_asexual* pour distinguer les Pokémons asexués de la caractéristique *gender_rate* (chances que le Pokémon soit femelle)
* éventuellement supprimer les caractéristiques redondantes (expérience de base, poids) et celles qui relèvent plutôt de mécaniques de jeu (bonheur, rythme de progression, taux de capture...)

---
## Évolution du projet

Le projet est en cours, ce fichier évoluera à mesure de ma progression.

__Étape en cours :__ élaboration du modèle

Étapes terminées :
* réflexion sur la pertinence et la faisabilité du projet
* extraction des données brutes depuis la PokéAPI (endpoits /pokemon et /pokemon-species)
* extraction des données pertinentes dans les fichiers JSON et conversion en un seul CSV
* analyse et visualisation de données avec Power BI, recommandations pour le modèle