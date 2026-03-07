


Point d'entrée : route espèces qui contient exactement les 1025 Pokémons officiels
Pour chaque espèce, récupérer les infos supplémentaires sur la route Pokemon associée



Caractéristiques référentielles :
- id → primary key
- name


PAGE ESPECE


Caractéristiques référentielles :
- names : pour la traduction EN-FR
- variétés : pokemons associés, seul le default nous intéresse (on exclut mega, gmax, etc.)


Caractéristiques numériques :
- taux de capture → à voir si ça ne fait pas doublon avec baby / légendaire / mythique
- base happiness → vérifier si certains types sont plus heureux par défaut que d'autres (ex: fée)
- chaine d'évolution + évolution précédente → variable niveau d'évolution 0/1/2 + variable booléenne has_evolution (un Pokémon 0 qui a une évolution sera plus faible qu'un Pokémon 0 n'ayant aucune évolution)
- gender rate : chance d'être femelle (sur 8) → vérifier le lien avec le type (pertinent pour Gallame/Gardevoir par exemple mais c'est un cas très spécifique)
- génération → peut-être juste informationnel, lien à vérifier
- growth rate : vitesse à laquelle le Pokémon gagne des niveaux → attention, corrélation ou éventuel doublon à vérifier
- is baby
- is lengendary
- is mythical
- hatch counter : multiplicateur pour le nombre de pas à marcher pour faire éclore l'oeuf → vérifier la corrélation (peut-être caractéristique + élevée pour les dragons par exemple ?)


Caractéristiques non pertinentes :
- couleur
- groupe d'oeufs → trop révélateur et précis
- description
- description de forme
- forme changeable
- genera : genus en plusieurs langues
- habitat : trop révélateur
- différences de genre visuelles
- n° Pokedex par version → trop complexe, on se concentre sur les caractéristiques individuelles
- pal park encounters → spécifique à une seule génération
- shape → pas pertinent




PAGE POKEMON

VARIABLE CIBLE :
- types


Caractéristiques numériques :
- base_experience : expérience donnée quand on bat ce Pokémon → vérifier la corrélation avec le type, Nanméouie en donne beaucoup mais est de type Normal, ne veut rien dire
- taille
- poids
- stats - base stats : HP, attack, special attack, defense, special defense, speed
- stats - effort → pas une caractéristique intrinsèque du Pokémon, plutôt un bonus donné au joueur, met l'accent sur une stat mais vérifier que ça ne fait pas doublon avec la stat qui a la meilleure base


Caractéristiques non pertinentes :
- espèces → référence unique pour les Pokémons déclinés en plusieurs variétés, pas nécessaire car on récupère d'abord l'espèce, ensuite les infos complémentaires dans /pokemon
- Talents → trop spécifique et révélateur ? 367 talents pour 1026 Pokémons
- Talents passés → idem
- cris → non
- formes → non
- n° Pokedex par version → trop complexe, on se concentre sur les caractéristiques individuelles
- objets tenus → trop spécifique et révélateur
- zones de rencontre → non
- is_default → Pokémon de référence pour l'espèce
- capacités → non, beaucoup trop fourni et révélateur
- types passés → non, on veut prédire les types actuels à partir des caractéristiques actuelles
- stats passées → non
- sprites → non
- ordre → Order for sorting. Almost national order, except families are grouped together. pas d'intérêt, on a accès aux évolutions sur la page espèces
