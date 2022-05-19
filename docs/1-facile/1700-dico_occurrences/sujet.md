---
author: BNS2022-10.1, puis Franck Chambon
title: Dictionnaire d'occurrences
tags:
  - dictionnaire
  - boucle
  - string
---
# Dictionnaire des nombres d'occurrences dans une phrase

!!! info "Occurrence d'un caractère dans une phrase"
    D'après Le Larousse : « En logique, place occupée par un symbole dans une formule. »

    - Le nombre d'occurrences du caractère `"o"` dans `"bonjour"` est 2 ;
    - le nombre d'occurrences du caractère `"b"` dans `"bonjour"` est 1 ;
    - le nombre d'occurrences du caractère `"B"` dans `"bonjour"` est 0 ;
    - le nombre d'occurrences du caractère `" "` dans `"Bonjour à tous !"` est 3.

On souhaite stocker les nombres d'occurrences dans un dictionnaire dont les clés sont les caractères de la phrase et les valeurs le nombre d'occurrences du caractère.

Écrire une fonction `occurrence_lettres` prenant comme paramètre une chaine de caractères `phrase`. Cette fonction doit renvoyer un dictionnaire des nombres d'occurrences des caractères présents dans `phrase`.

!!! example "Exemples"

    ```pycon
    >>> occurrence_lettres("Bonjour à tous !") == {'B': 1, 'o': 3, 'n': 1, 'j': 1, 'u': 2, 'r': 1, ' ': 3, 'à': 1, 't': 1, 's': 1, '!': 1}
    True
    ```
    ```pycon
    >>> occurrence_lettres("ababbab") == {"a": 3, "b": 4}
    True
    ```
    
    On rappelle que l'ordre des clés n'a pas d'importance pour comparer deux dictionnaires.


{{ IDE('exo') }}
